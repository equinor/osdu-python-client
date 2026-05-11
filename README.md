# OSDU Python Client

[![SCM Compliance](https://scm-compliance-api.radix.equinor.com/repos/equinor/060070c2-8a92-457a-bf34-8c625391b777/badge)](https://developer.equinor.com/governance/scm-policy/)

This project is a Python client library for [OSDU](https://osduforum.org/) services, automatically generated from OpenAPI specifications using [openapi-python-client](https://github.com/openapi-generators/openapi-python-client) and wrapped with a thin handwritten facade that handles authentication, retries, partition headers, and ergonomic per-operation calls.

## Generated code is not committed

The Python clients under `src/osdu_python_client/generated/` are produced by running `openapi-python-client` against the OpenAPI specs in `openapi_specs/`. This output is **not committed to the repository** for the following reasons:

- **Nobody can accidentally edit it.** If the generated code is not in the repository, it cannot be hand-edited. Any change must go through the spec and the generator — the only correct way to change it.
- **The spec is the source of truth.** Committing generated code creates a second source of truth that can silently drift from the spec.
- **Diffs stay meaningful.** A spec change generates hundreds of touched lines across dozens of files. Keeping generated code out of git means pull request diffs show only what actually changed.
- **Reproducible by design.** Given the same spec and the same generator version, generation is deterministic. Storing the result is redundant.

Consumers of the published package can browse the generated client code through their IDE or AI coding assistant after installing it. Contributors working in this repository should run the generation script once after cloning to have the generated code available locally.

## Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) for dependency management and scripts

## Installation

```bash
uv sync --all-extras
uv run python generate_all.py
```

## Quick Start

```python
from osdu_python_client import OsduClient
from osdu_python_client.generated.search.models.query_request import QueryRequest

with OsduClient() as osdu:  # config from .env
    dto = osdu.search.query_records(
        body=QueryRequest(kind="osdu:wks:master-data--Wellbore:*", query="*", limit=1)
    )
    for record in dto.results:
        print(record.additional_properties)
```

Each `osdu.<service>.<operation>(...)` call auto-binds the underlying client and `data-partition-id`, returns the parsed response on 2xx, and raises `OsduError` on non-2xx. `.detailed(...)` on any operation returns the full `Response` envelope.

For async usage, auth providers (Azure / AWS / GCP / IBM), debugging, per-service header overrides, and the low-level raw client escape hatch, see [docs/usage.md](docs/usage.md).

## Available Services

| Attribute        | Service                    |
| ---------------- | -------------------------- |
| `crs_catalog`    | CRS Catalog                |
| `crs_conversion` | CRS Conversion             |
| `dataset`        | Dataset                    |
| `entitlements`   | Entitlements               |
| `file`           | File                       |
| `indexer`        | Indexer                    |
| `workflow`       | Ingestion Workflow Service |
| `legal`          | Legal                      |
| `notification`   | Notification               |
| `partition`      | Partition                  |
| `policy`         | Policy                     |
| `register`       | Register                   |
| `schema`         | Schema                     |
| `search`         | Search                     |
| `storage`        | Storage                    |
| `unit`           | Unit                       |
| `wellbore_ddms`  | Wellbore DDMS              |

## Running Tests

```bash
uv run pytest
```

For `.env` setup, optional variables, and detailed test commands, see [docs/environment-and-tests.md](docs/environment-and-tests.md).

## Development

Quick flow:

```bash
git clone https://github.com/equinor/osdu-python-client.git
cd osdu-python-client
uv sync --all-extras
uv run python generate_all.py
uv run pytest
```

For release flow, OpenAPI update steps, response media type normalization, client regeneration, adding new services, and project structure, see [docs/development.md](docs/development.md).

## Documentation

- Usage examples (facade, async, auth, debugging, raw client): [docs/usage.md](docs/usage.md)
- Environment and tests: [docs/environment-and-tests.md](docs/environment-and-tests.md)
- Development and release workflow: [docs/development.md](docs/development.md)

## License

Ref. [License Information](LICENSE)
