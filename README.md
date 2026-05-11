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

# Optional endpoint overrides (defaults defined in src/osdu_python_client/services/registry.py)
# endpoint_overrides='{"search": "/api/search/v3", "wellbore_ddms": "/api/os-wellbore-ddms-staging"}'
```

## Usage

Two layers are available:

1. **`osdu_python_client.OsduClient`** — recommended. A facade that handles auth (MSAL), partition headers, retries with exponential backoff and `Retry-After`, a shared connection pool across all services, and ergonomic per-operation method dispatch.
2. **`osdu_python_client.generated.<service>.AuthenticatedClient`** — the raw generated clients. Use directly when you want to bring your own httpx setup.

### Recommended: `OsduClient`

```python
from osdu_python_client import OsduClient
from osdu_python_client.generated.search.models.query_request import QueryRequest

with OsduClient() as osdu:  # config loaded from .env
    dto = osdu.search.query_records(
        body=QueryRequest(kind="osdu:wks:master-data--Wellbore:*", query="*", limit=1)
    )
    for record in dto.results:
        print(record.additional_properties)
```

Each `osdu.<service>.<operation>(...)` call auto-binds the underlying client and `data-partition-id`, returns the parsed response model on 2xx, and raises `OsduError` on non-2xx. Available services: `crs_catalog`, `crs_conversion`, `dataset`, `entitlements`, `file`, `indexer`, `legal`, `notification`, `partition`, `policy`, `register`, `schema`, `search`, `storage`, `unit`, `wellbore_ddms`, `workflow`.

If you need the full `Response` envelope (status code, headers, raw parsed error model), call `.detailed`:

```python
result = osdu.search.query_records.detailed(body=request)
print(result.status_code, result.headers)
```

`osdu.<service>.raw` is the underlying `AuthenticatedClient` if you ever need it.

### Async

```python
import asyncio
from osdu_python_client import AsyncOsduClient
from osdu_python_client.generated.search.models.query_request import QueryRequest

async def main():
    async with AsyncOsduClient() as osdu:
        dto = await osdu.search.query_records(
            body=QueryRequest(kind="osdu:wks:master-data--Wellbore:*", query="*", limit=1)
        )
        return dto.results

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

### Debugging

The library logs through Python's standard `logging` module. Loggers used:

| Logger                                       | Level   | What it emits                                                |
|----------------------------------------------|---------|--------------------------------------------------------------|
| `osdu_python_client.transport`               | DEBUG   | every request/response with method, URL, status, timing      |
| `osdu_python_client.transport`               | INFO    | retry decisions, 401 → token refresh                         |
| `osdu_python_client.transport`               | WARNING | retries exhausted                                            |
| `osdu_python_client.transport.body`          | DEBUG   | request/response bodies (truncated to ~2KB)                  |
| `osdu_python_client.auth`                    | DEBUG   | token acquisition (cache hit / fresh, never the token value) |

`Authorization`, `Cookie`, `Set-Cookie`, and `Proxy-Authorization` headers are redacted from log output. Bodies are off by default (gated on a separate child logger) because OSDU payloads often contain PII.

For a quick one-call setup:

```python
from osdu_python_client import enable_debug_logging
enable_debug_logging()                          # transport + auth at DEBUG, bodies stay off
enable_debug_logging(include_bodies=True)       # also log truncated bodies
```

Production consumers should skip the helper and configure handlers/formatters via `logging.config` directly.

For wire-level visibility below the library, also raise `httpx` / `httpcore`:

```python
import logging
logging.getLogger("httpx").setLevel(logging.DEBUG)
logging.getLogger("httpcore").setLevel(logging.DEBUG)
```

For custom per-request observation (tracing, metrics), attach event hooks on the underlying httpx client: `osdu.<service>.get_httpx_client().event_hooks["request"].append(...)`.

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

### Adding a new service

1. Drop the OpenAPI JSON spec into `openapi_specs/`.
2. Run `uv run python generate_all.py`.
3. Add one line to `SERVICE_REGISTRY` in [`src/osdu_python_client/services/registry.py`](src/osdu_python_client/services/registry.py) declaring the facade attribute name and the default endpoint path. The new operations become callable as `osdu.<attr>.<operation_id>(...)` automatically — no per-service wrapper code.

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
