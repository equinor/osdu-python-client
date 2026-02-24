# OSDU Python Client

This project is a Python client for [OSDU](https://osduforum.org/) services, automatically generated from OpenAPI specifications using [openapi-python-client](https://github.com/openapi-generators/openapi-python-client).

It provides typed, async-ready clients for various OSDU core services, allowing for easy integration with OSDU APIs in Python applications.

## Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) (for dependency management and running scripts)

## Installation

This project is managed with `uv`. To install dependencies:

```bash
uv sync --all-extras
```

## .env Setup

Integration tests and local examples can load configuration from a `.env` file in the repository root (via Pydantic Settings in `tests/config.py`).

Create `.env` with the required values for your OSDU environment:

```dotenv
# Base OSDU host (no trailing slash)
server=https://your-osdu-instance.com

# Required for authenticated test runs
data_partition_id=your-partition-id
authority=https://login.microsoftonline.com/<tenant-id>
scopes=api://<app-id-uri>/.default
client_id=<public-client-id>

# Optional endpoint overrides (defaults are defined in tests/config.py)
# crs_catalog_endpoint=/api/crs/catalog/v2
# crs_converter_endpoint=/api/crs/converter/v2
# entitlements_endpoint=/api/entitlements/v2
# file_endpoint=/api/file/v2
# legal_endpoint=/api/legal/v1
# schema_endpoint=/api/schema/v1/
# search_endpoint=/api/search/v2
# storage_endpoint=/api/storage/v2
# unit_endpoint=/api/unit/v3
# workflow_endpoint=/api/workflow/v1
```

Optional environment variables used by tests:

- `OSDU_MSAL_CACHE_PATH`: Path to a persistent MSAL token cache file (default: `.msal_token_cache.bin` in repo root)

## Usage

Each OSDU service has its own sub-package under `osdu_python_client`.

### Example: Entitlements Service

```python
import asyncio

from osdu_python_client.entitlements.api.list_group_on_behalf_of_api import (
    list_all_partition_groups,
)
from osdu_python_client.entitlements.client import AuthenticatedClient

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

This command runs `generate_all.py`, which iterates through the JSON files and uses `openapi-python-client` to generate the code into `osdu_python_client/`. It also handles minor patching of specs (e.g., missing versions) to ensure successful generation.

Warning: do not hand-edit files under `src/osdu_python_client/`. They are generated artifacts and your changes will be overwritten the next time `uv run python generate_all.py` is run. Make changes in `openapi_specs/` and/or the generation scripts instead.

## Project Structure

- `openapi_specs/`: Contains the downloaded OpenAPI JSON specifications.
- `fix_openapi_json_response_media_types.py`: Helper script to normalize `*/*` response media types to `application/json` for structured JSON responses in specs.
- `src/osdu_python_client/`: The generated Python package containing clients for each service.
- `download.py`: Script to download specs.
- `generate_all.py`: Script to generate the clients.
- `pyproject.toml`: Project configuration and dependencies (managed by `uv`).

## License

Ref. [License Information](LICENSE)
