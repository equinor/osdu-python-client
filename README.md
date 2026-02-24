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

## Usage

Each OSDU service has its own sub-package under `osdu_python_client`.

### Example: Entitlements Service

```python
from osdu_python_client.entitlements.client import AuthenticatedClient
from osdu_python_client.entitlements.api.groups import list_groups

# Initialize the client
client = AuthenticatedClient(
    base_url="https://your-osdu-instance.com/api/entitlements/v2",
    token="YOUR_ACCESS_TOKEN"
)

# Call an API endpoint (synchronous)
response = list_groups.sync(client=client, data_partition_id="your-partition-id")
if response:
    print(response.groups)

# Call an API endpoint (asynchronous)
import asyncio

async def main():
    response = await list_groups.asyncio(client=client, data_partition_id="your-partition-id")
    if response:
        print(response.groups)

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

### Regenerating Clients

To regenerate the Python clients from the specifications in `openapi_specs/`:

```bash
uv run python generate_all.py
```

This command runs `generate_all.py`, which iterates through the JSON files and uses `openapi-python-client` to generate the code into `osdu_python_client/`. It also handles minor patching of specs (e.g., missing versions) to ensure successful generation.

## Project Structure

- `openapi_specs/`: Contains the downloaded OpenAPI JSON specifications.
- `osdu_python_client/`: The generated Python package containing clients for each service.
- `download.py`: Script to download specs.
- `generate_all.py`: Script to generate the clients.
- `pyproject.toml`: Project configuration and dependencies (managed by `uv`).

## License

Ref. [License Information](LICENSE)
