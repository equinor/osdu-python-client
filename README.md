# OSDU Python Client

[![SCM Compliance](https://scm-compliance-api.radix.equinor.com/repos/equinor/060070c2-8a92-457a-bf34-8c625391b777/badge)](https://developer.equinor.com/governance/scm-policy/)

This project is a Python client for [OSDU](https://osduforum.org/) services, automatically generated from OpenAPI specifications using [openapi-python-client](https://github.com/openapi-generators/openapi-python-client).

It provides typed, async-ready clients for various OSDU core services, allowing for easy integration with OSDU APIs in Python applications.

## Generated code is not committed

The Python clients under `src/` are produced by running `openapi-python-client` against the OpenAPI specs in `openapi_specs/`. This output is **not committed to the repository** for the following reasons:

- **Nobody can accidentally edit it.** If the generated code is not in the repository, it cannot be hand-edited. Any change must go through the spec and the generator — the only correct way to change it.
- **The spec is the source of truth.** Committing generated code creates a second source of truth that can silently drift from the spec.
- **Diffs stay meaningful.** A spec change generates hundreds of touched lines across dozens of files. Keeping generated code out of git means pull request diffs show only what actually changed.
- **Reproducible by design.** Given the same spec and the same generator version, generation is deterministic. Storing the result is redundant.

Consumers of the published package can browse the generated client code through their IDE or AI coding assistant after installing it. Contributors working in this repository should run the generation script once after cloning to have the generated code available locally.

## Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) (for dependency management and running scripts)

## Installation

This project is managed with `uv`. To install dependencies:

```bash
uv sync --all-extras
```

## .env Setup

`OsduClient` (and the legacy test fixtures) load configuration from a `.env` file in the repository root via Pydantic Settings.

Create `.env` with the required values for your OSDU environment:

```dotenv
# Base OSDU host (no trailing slash)
server=https://your-osdu-instance.com

# Partition + auth
data_partition_id=your-partition-id
authority=https://login.microsoftonline.com/<tenant-id>
scopes=api://<app-id-uri>/.default
client_id=<public-client-id>

# Auth mode: interactive (default) | device_flow | client_credentials
auth_mode=interactive
# client_secret=<required only for client_credentials>

# MSAL token cache (default: .msal_token_cache.bin)
# msal_cache_path=.msal_token_cache.bin

# Retry/timeout tuning
# timeout_seconds=30
# retry_attempts=3
# retry_base_delay=0.5
# verify_ssl=true

# Optional endpoint overrides (defaults defined in src/osdu_python_client/config.py)
# search_endpoint=/api/search/v2
# storage_endpoint=/api/storage/v2
# wellbore_ddms_endpoint=/api/os-wellbore-ddms
# ...one per service
```

## Usage

Two layers are available:

1. **`osdu_python_client.OsduClient`** — recommended. A thin facade that handles auth (MSAL), partition headers, retries with exponential backoff and `Retry-After`, and a single shared connection pool across all services.
2. **`osdu_python_client.generated.<service>.AuthenticatedClient`** — the raw generated clients. Use directly when you want to bring your own httpx setup.

### Recommended: `OsduClient`

```python
from osdu_python_client import OsduClient
from osdu_python_client.generated.search.api.search_api import query_records
from osdu_python_client.generated.search.models.query_request import QueryRequest

with OsduClient() as osdu:  # config loaded from .env
    result = query_records.sync_detailed(
        client=osdu.search,
        body=QueryRequest(kind="osdu:wks:master-data--Wellbore:*", query="*", limit=1),
        data_partition_id=osdu.config.data_partition_id,
    )
```

`osdu.<service>` returns the generated `AuthenticatedClient` for that service, pre-wired with retry transport and `data-partition-id` defaulting. Available service properties: `crs_catalog`, `crs_conversion`, `dataset`, `entitlements`, `file`, `indexer`, `legal`, `notification`, `partition`, `policy`, `register`, `schema`, `search`, `storage`, `unit`, `wellbore_ddms`, `workflow`.

### Async

```python
import asyncio
from osdu_python_client import AsyncOsduClient
from osdu_python_client.generated.search.api.search_api import query_records
from osdu_python_client.generated.search.models.query_request import QueryRequest

async def main():
    async with AsyncOsduClient() as osdu:
        result = await query_records.asyncio_detailed(
            client=osdu.search,
            body=QueryRequest(kind="osdu:wks:master-data--Wellbore:*", query="*", limit=1),
            data_partition_id=osdu.config.data_partition_id,
        )

asyncio.run(main())
```

### Auth modes

`OsduConfig.auth_mode` (env var `AUTH_MODE`) selects the MSAL flow. All three persist tokens to `msal_cache_path` (default `.msal_token_cache.bin`).

| Mode                  | When to use            | Required config                            |
|-----------------------|------------------------|--------------------------------------------|
| `interactive`         | Local dev / tests      | `client_id`, `authority`, `scopes`         |
| `device_flow`         | Headless ops scripts   | `client_id`, `authority`, `scopes`         |
| `client_credentials`  | CI, service-to-service | + `client_secret`                          |

```python
# Interactive (default)
osdu = OsduClient()

# Client credentials — set AUTH_MODE=client_credentials and CLIENT_SECRET=... in env, or:
from osdu_python_client import ClientCredentialsProvider, OsduConfig
config = OsduConfig(auth_mode="client_credentials", client_secret="…")
osdu = OsduClient(config=config, token_provider=ClientCredentialsProvider(config))

# Bring your own provider — anything with .get_token(force_refresh: bool) -> str works
class MyProvider:
    def get_token(self, force_refresh: bool = False) -> str:
        return "…"

osdu = OsduClient(token_provider=MyProvider())
```

Tokens are injected per-request, so refresh after a 401 takes effect immediately. The transport retries 401 once with `force_refresh=True` and retries `429/502/503/504` with backoff honouring `Retry-After`.

### Per-service header overrides

Some endpoints accept extra headers (e.g. `frame-of-reference` on CRS). Use the `with_headers` context manager — it scopes mutations to one or all built service clients and restores them on exit.

```python
with osdu.with_headers(service="crs_conversion", **{"frame-of-reference": "units=SI"}):
    convert_records.sync_detailed(client=osdu.crs_conversion, body=req,
                                  data_partition_id=osdu.config.data_partition_id)

# Or apply to every service client built so far (e.g. correlation IDs):
with osdu.with_headers(**{"x-correlation-id": correlation_id}):
    ...
```

The async client exposes the same helper as `async with osdu.with_headers(...)`.

### Low-level: raw `AuthenticatedClient`

The generated clients can also be used directly with a static token (no retry, no auto-refresh, no shared connection pool):

```python
import asyncio

from osdu_python_client.generated.entitlements.api.list_group_on_behalf_of_api import (
    list_all_partition_groups,
)
from osdu_python_client.generated.entitlements.client import AuthenticatedClient

# Initialize the client
client = AuthenticatedClient(
    base_url="https://your-osdu-instance.com/api/entitlements/v2",
    token="YOUR_ACCESS_TOKEN"
)

# Call an API endpoint (synchronous, detailed response wrapper)
result = list_all_partition_groups.sync_detailed(
    client=client,
    data_partition_id="your-partition-id",
    type_="NONE",  # Optional filter; adjust for your deployment
)
if result.parsed:
    for group in result.parsed.groups:
        print(group.name, group.email)

# Or use the async version:
async def main():
    result = await list_all_partition_groups.asyncio_detailed(
        client=client,
        data_partition_id="your-partition-id",
        type_="NONE",
    )
    if result.parsed:
        for group in result.parsed.groups:
            print(group.name, group.email)

if __name__ == "__main__":
    asyncio.run(main())
```

### Available Services

The following services are currently generated:

- `crs_catalog`
- `crs_conversion`
- `dataset`
- `entitlements`
- `file`
- `indexer`
- `ingestion_workflow_service`
- `legal`
- `notification`
- `partition`
- `policy`
- `register`
- `schema`
- `search`
- `storage`
- `unit`
- `wellbore_ddms`

## Development

### Updating OpenAPI Specs

To fetch the latest OpenAPI specifications from the OSDU wiki:

```bash
uv run python download.py
```

This script parses the OSDU wiki for service definitions and downloads the corresponding JSON specs into the `openapi_specs/` directory.

Warning: the raw upstream specs are not always generator-friendly. This repository may intentionally apply local edits to files in `openapi_specs/` to improve generated model quality and parsing behavior.

### Normalizing OpenAPI Response Media Types

The repository includes `fix_openapi_json_response_media_types.py` to patch a common issue in downloaded specs: some endpoints declare structured JSON responses under `*/*` instead of `application/json`.

This matters because incorrect response media types can lead to weaker or incorrect generated client parsing/typing.

Check what would be changed:

```bash
uv run python fix_openapi_json_response_media_types.py --check
```

Apply fixes to specs in `openapi_specs/`:

```bash
uv run python fix_openapi_json_response_media_types.py
```

You can also target a specific file:

```bash
uv run python fix_openapi_json_response_media_types.py openapi_specs/Search.json
```

### Regenerating Clients

To regenerate the Python clients from the specifications in `openapi_specs/`:

```bash
uv run python generate_all.py
```

This command runs `generate_all.py`, which iterates through the JSON files and uses `openapi-python-client` to generate the code into `src/osdu_python_client/generated/`. It also handles minor patching of specs (e.g., missing versions) to ensure successful generation.

Warning: do not hand-edit files under `src/osdu_python_client/generated/`. They are generated artifacts and your changes will be overwritten the next time `uv run python generate_all.py` is run. Make changes in `openapi_specs/` and/or the generation scripts instead.

### Releasing a new version

Releases are automated using [Release Please](https://github.com/googleapis/release-please).

**How it works:**

1. On merge to `main`, Release Please checks new commits since the last release using the [Conventional Commits](https://www.conventionalcommits.org/) format.
2. When releasable changes are found, Release Please creates or updates a release pull request that bumps the version in [`pyproject.toml`](pyproject.toml) and updates [`CHANGELOG.md`](CHANGELOG.md).
3. When the release pull request is merged, the release workflow creates a GitHub release and publishes the NuGet package.

## Project Structure

- `openapi_specs/`: Contains the downloaded OpenAPI JSON specifications.
- `fix_openapi_json_response_media_types.py`: Helper script to normalize `*/*` response media types to `application/json` for structured JSON responses in specs.
- `src/osdu_python_client/`: Public package — handwritten facade (`OsduClient`, config, transport, auth, services wrappers) at the top level, plus a `generated/` subpackage produced by `generate_all.py`. Do not hand-edit files under `src/osdu_python_client/generated/`.
- `download.py`: Script to download specs.
- `generate_all.py`: Script to generate the clients.
- `pyproject.toml`: Project configuration and dependencies (managed by `uv`).

## License

Ref. [License Information](LICENSE)
