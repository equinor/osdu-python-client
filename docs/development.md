# Development

## Getting Started

Clone the repo, sync dependencies, generate the clients, run the tests:

```bash
git clone https://github.com/equinor/osdu-python-client.git
cd osdu-python-client
uv sync --all-extras
uv run python generate_all.py
uv run pytest
```

Copy `.env.example` to `.env` (or create manually) and fill in your OSDU environment values before running integration tests — see [environment-and-tests.md](environment-and-tests.md).

## Adding a New Service

1. Drop the OpenAPI spec (`.json`, `.yaml`, or `.yml`) into `openapi_specs/`.
2. Run `uv run python generate_all.py`.
3. Add one line to `SERVICE_REGISTRY` in [`src/osdu_python_client/services/registry.py`](../src/osdu_python_client/services/registry.py) declaring the facade attribute name and the default endpoint path.

The new operations become callable as `osdu.<attr>.<operation_id>(...)` automatically — no per-service wrapper code, no config changes, no test scaffolding.

## Updating OpenAPI Specs

To fetch the latest OpenAPI specifications from the OSDU wiki:

```bash
uv run python download.py
```

This script parses the OSDU wiki for service definitions and downloads the corresponding JSON specs into `openapi_specs/`.

> Warning: the raw upstream specs are not always generator-friendly. This repository may intentionally apply local edits to files in `openapi_specs/` to improve generated model quality and parsing behavior. Check `git diff` after running `download.py` before committing.

## Normalizing OpenAPI Response Media Types

Some OSDU endpoints declare structured JSON responses under `*/*` instead of `application/json`. Wrong response media types lead to weaker or incorrect generated client parsing/typing. The included script fixes these in place:

```bash
# Dry-run — show what would change
uv run python fix_openapi_json_response_media_types.py --check

# Apply fixes to all specs
uv run python fix_openapi_json_response_media_types.py

# Target a specific file
uv run python fix_openapi_json_response_media_types.py openapi_specs/Search.json
```

## Regenerating Clients

To regenerate the Python clients from the specs in `openapi_specs/`:

```bash
uv run python generate_all.py
```

The script iterates through both JSON and YAML specs and uses `openapi-python-client` to generate code into `src/osdu_python_client/generated/<service>/`. It also handles minor patching (missing `info.version`, YAML timestamp normalization) before invoking the generator.

> Warning: do not hand-edit files under `src/osdu_python_client/generated/`. They are generated artifacts and your changes will be overwritten the next time `generate_all.py` runs. Make changes in `openapi_specs/` and/or the generation scripts instead.

## Releasing a New Version

Releases are automated using [Release Please](https://github.com/googleapis/release-please).

How it works:

1. On merge to `main`, Release Please checks new commits since the last release using the [Conventional Commits](https://www.conventionalcommits.org/) format.
2. When releasable changes are found, Release Please creates or updates a release pull request that bumps the version in [`pyproject.toml`](../pyproject.toml) and updates [`CHANGELOG.md`](../CHANGELOG.md).
3. When the release pull request is merged, the release workflow creates a GitHub release and publishes the package.

## Project Structure

```txt
openapi_specs/                                 OpenAPI specifications (.json / .yaml / .yml)
src/
    osdu_python_client/
        __init__.py                            Public package surface
        client.py                              OsduClient facade (sync)
        async_client.py                        AsyncOsduClient facade
        config.py                              CSP-agnostic OsduConfig
        transport.py                           Retry + auth + body logging
        hooks.py                               httpx request hooks (partition header)
        errors.py                              OsduError hierarchy
        logging_setup.py                       enable_debug_logging helper
        auth/                                  Pluggable auth providers
            _base.py                           TokenProvider Protocol + registry
            azure.py                           MSAL providers + AzureMsalConfig
            aws.py / gcp.py / ibm.py           Stubs for AWS / GCP / IBM
        services/                              Facade plumbing
            facade.py                          ServiceFacade + Endpoint proxy
            registry.py                        SERVICE_REGISTRY (one line per service)
        generated/                             Generated clients (gitignored)
tests/
    test_facade.py / test_transport.py / test_logging.py   Unit tests (no network)
    search_test.py / entitlements_test.py                  Integration tests
    osdu_fixture.py / auth_fixture.py / config.py          Test fixtures
download.py                                   Downloads specs from the OSDU wiki
fix_openapi_json_response_media_types.py      Normalizes */* response media types
generate_all.py                               Regenerates all Python clients
```
