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

This repository has two layers, both housed under one public package `osdu_python_client`: a handwritten facade at the top level, and an OpenAPI-generated tree under `osdu_python_client.generated`.

**Spec-driven generation pipeline** (`src/osdu_python_client/generated/<service>/` is the generator output and **not committed** — run `generate_all.py` after cloning):

- `openapi_specs/*.json` are the source inputs for each OSDU service.
- `download.py` fetches the OSDU Core Services wiki, extracts service doc links, normalizes `swagger-ui`/`/docs` URLs to JSON spec endpoints, and downloads specs with provider fallbacks (`ci`, `azure`, `aws`, `gc`).
- `fix_openapi_json_response_media_types.py` patches a recurring upstream issue where structured JSON responses are declared under `*/*` instead of `application/json`. It only rewrites 2xx responses whose schemas resolve to structured payloads.
- `generate_all.py` regenerates `src/osdu_python_client/generated/<service>/` for every spec (`PACKAGE_DIR = src/osdu_python_client/generated`). It also patches missing `info.version` values before invoking `openapi-python-client`.

Generated service packages follow the same shape:

- `client.py` defines `Client` and `AuthenticatedClient`.
- `api/` contains per-endpoint modules with `_get_kwargs`, `_parse_response`, `sync_detailed`, `sync`, `asyncio_detailed`, and `asyncio`.
- `models/` contains generated request/response DTOs.
- `types.py` and `errors.py` provide shared response wrappers and error handling.

**Handwritten facade** (top level of `src/osdu_python_client/`) is the recommended consumer entry point and wraps the generated clients:

- `OsduClient` / `AsyncOsduClient` (`client.py`, `async_client.py`) expose lazy per-service attributes (`osdu.search`, `osdu.storage`, …) via `__getattr__` driven by `services/registry.py`. Each returns a generated `AuthenticatedClient` (optionally wrapped in an ergonomic `services/<name>.py` class) pre-wired with a shared httpx connection pool, retry transport, and `data-partition-id` defaulting.
- `services/registry.py` is the single source of truth wiring facade attribute → generated module → config URL attribute → optional sync/async wrapper. Adding a new service is one `ServiceSpec` entry plus a `<name>_endpoint` + `<name>_url` in `OsduConfig`.
- `config.py` (Pydantic Settings) loads `.env` from the repo root: `server`, `data_partition_id`, MSAL settings (`authority`, `client_id`, `scopes`, `auth_mode`, optional `client_secret`), `*_endpoint` overrides, and retry/timeout tuning.
- `auth.py` provides `MsalInteractiveProvider`, `MsalDeviceFlowProvider`, and `ClientCredentialsProvider`, all backed by an MSAL token cache at `msal_cache_path` (default `.msal_token_cache.bin`). Any object with `get_token(force_refresh: bool) -> str` can be passed as `token_provider=`.
- `transport.py` / `hooks.py` inject the bearer token per-request, retry 401 once with `force_refresh=True`, and retry `429/502/503/504` with exponential backoff honouring `Retry-After`.
- `services/` holds optional ergonomic wrappers around the generated API modules (currently only `SearchService` / `AsyncSearchService`) that bind `data_partition_id`, expose `*_detailed` + unwrapped variants, and forward unknown attributes to the underlying generated client via `_ServiceBase.__getattr__`.
- `with_headers(service=None, **headers)` is a (sync/async) context manager scoping header mutations to one or all built service clients.

The `tests/` directory contains integration tests that exercise both layers against a live OSDU environment.

## Key conventions

- Treat `src/osdu_python_client/generated/` as generated output — never hand-edit. Change `openapi_specs/`, `download.py`, `fix_openapi_json_response_media_types.py`, or `generate_all.py`, then regenerate. Subpackages under `generated/` are gitignored; consumers regenerate locally (only the empty `generated/__init__.py` is committed so the namespace exists).
- Handwritten code lives at the top level of `src/osdu_python_client/`. Bug fixes and new features for the facade layer go here.
- Adding a new service: append a `ServiceSpec` to `services/registry.py`, add `<name>_endpoint` + `<name>_url` to `OsduConfig`, regenerate. Both `OsduClient` and `AsyncOsduClient` pick it up automatically via `__getattr__` — no per-service property definitions needed.
- When running tests, target `tests/` explicitly. Running `pytest` from the repo root also discovers generated `test_*.py` modules under `src/osdu_python_client/generated/register/`, which produces collection warnings unrelated to the handwritten test suite.
- Service package names come from spec filenames normalized to lowercase with spaces/hyphens converted to underscores, e.g. `Ingestion_Workflow_Service.json` becomes `osdu_python_client.generated.ingestion_workflow_service` (exposed as `osdu.workflow` on the facade).
- Repository tests are integration tests against a live OSDU environment, not isolated unit tests. Expect real network calls, `data_partition_id` headers, and MSAL auth (interactive by default; tokens cached to `.msal_token_cache.bin`, or `OSDU_MSAL_CACHE_PATH`). The exception is `tests/test_facade.py` and `tests/test_transport.py`, which use mocked transports and run offline.
- Generated endpoint helpers return a `Response[...]` wrapper from `sync_detailed(...)` / `asyncio_detailed(...)`; the parsed DTO is on `.parsed`. Tests assert on `result.status_code.value` and then work with `result.parsed`.
- Python 3.13+ is required.
- Commits use [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `deps:`, `docs:`, `chore:`, …). Release Please cuts releases from `main` based on commit types and updates `pyproject.toml` + `CHANGELOG.md` via PR.
