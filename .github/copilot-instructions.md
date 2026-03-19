# OSDU Python Client

## Build, test, and lint commands

```bash
uv sync --all-extras
uv run ruff check .
uv build
uv run pytest tests -q
uv run pytest tests/search_test.py::test_search_query_records -q
```

Integration tests depend on a repo-root `.env` loaded by `tests/config.py` and use MSAL interactive login from `tests/auth_fixture.py`. Tokens are cached in `.msal_token_cache.bin` by default, or at `OSDU_MSAL_CACHE_PATH` if set.

Useful repository-specific maintenance commands:

```bash
uv run python download.py
uv run python fix_openapi_json_response_media_types.py --check
uv run python fix_openapi_json_response_media_types.py
uv run python generate_all.py
```

## High-level architecture

This repository is organized around OpenAPI-driven client generation rather than handwritten runtime code.

- `openapi_specs/*.json` are the source inputs for each OSDU service.
- `download.py` fetches the OSDU Core Services wiki, extracts service doc links, normalizes `swagger-ui`/`/docs` URLs to JSON spec endpoints, and downloads specs with provider fallbacks (`ci`, `azure`, `aws`, `gc`).
- `fix_openapi_json_response_media_types.py` patches a recurring upstream issue where structured JSON responses are declared under `*/*` instead of `application/json`. It only rewrites 2xx responses whose schemas resolve to structured payloads.
- `generate_all.py` regenerates `src/osdu_python_client/<service>/` for every spec. It also patches missing `info.version` values before invoking `openapi-python-client`.

Generated service packages follow the same shape:

- `client.py` defines `Client` and `AuthenticatedClient`.
- `api/` contains per-endpoint modules with `_get_kwargs`, `_parse_response`, `sync_detailed`, `sync`, `asyncio_detailed`, and `asyncio`.
- `models/` contains generated request/response DTOs.
- `types.py` and `errors.py` provide shared response wrappers and error handling.

The handwritten test layer in `tests/` is the main example of intended usage. `tests/config.py` builds service URLs from a single `server` plus `*_endpoint` settings, `tests/auth_fixture.py` acquires an Azure access token with MSAL, and tests instantiate a service-specific `AuthenticatedClient` before calling generated endpoint functions and inspecting `result.parsed`.

## Key conventions

- Treat `src/osdu_python_client/` as generated output. Prefer changing `openapi_specs/`, `download.py`, `fix_openapi_json_response_media_types.py`, or `generate_all.py`, then regenerate.
- When running tests, target `tests/` explicitly. Running `pytest` from the repo root also discovers generated `test_*.py` modules under `src/osdu_python_client/register/`, which produces collection warnings unrelated to the handwritten test suite.
- Service package names come from spec filenames normalized to lowercase with spaces/hyphens converted to underscores, e.g. `Ingestion_Workflow_Service.json` becomes `osdu_python_client.ingestion_workflow_service`.
- Repository tests are integration tests against a live OSDU environment, not isolated unit tests. Expect real network calls, `data_partition_id` headers, and interactive authentication if no cached MSAL token is available.
- Generated endpoint helpers usually return a `Response[...]` wrapper from `sync_detailed(...)`; the parsed DTO is available on `.parsed`. Existing tests assert on `result.status_code.value` and then work with `result.parsed`.
