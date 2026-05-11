# Environment and Tests

## .env Setup

`OsduClient` and the integration test fixtures load configuration from a `.env` file in the repository root via Pydantic Settings.

Create `.env` with the required values for your OSDU environment:

```dotenv
# Base OSDU host (no trailing slash)
SERVER=https://your-osdu-instance.com

# Required
DATA_PARTITION_ID=your-partition-id

# Azure auth (default provider — see docs/usage.md "Auth Providers" for other CSPs)
AUTHORITY=https://login.microsoftonline.com/<tenant-id>
CLIENT_ID=<public-client-id>
SCOPES=api://<app-id-uri>/.default

# MSAL flow: interactive (default) | device_flow | client_credentials
AUTH_MODE=interactive
# CLIENT_SECRET=<required only for client_credentials>
```

### Optional environment variables

Used by `OsduClient` / `OsduConfig`:

- `AUTH_PROVIDER` — auth provider name (default: `azure_msal`). One of `azure_msal`, `aws_cognito`, `gcp_iam`, `ibm_iam`, or any provider registered via `register_provider()`.
- `MSAL_CACHE_PATH` — persistent MSAL token cache file (default: `.msal_token_cache.bin`).
- `TIMEOUT_SECONDS` — per-request timeout in seconds (default: `30.0`).
- `RETRY_ATTEMPTS` — max retry attempts on 429/502/503/504 (default: `3`).
- `RETRY_BASE_DELAY` — initial backoff delay in seconds (default: `0.5`).
- `VERIFY_SSL` — TLS certificate verification (default: `true`).
- `ENDPOINT_OVERRIDES` — JSON dict overriding default service endpoints, e.g. `'{"search": "/api/search/v3"}'`. Defaults defined in `src/osdu_python_client/services/registry.py`.

Used by integration tests:

- `OSDU_MEMBER_EMAIL` — your work email; required by the entitlements integration test (`list_groups_on_behalf_of`).
- `OSDU_SEARCH_KIND` — kind filter for search tests (default: `osdu:wks:work-product-component--WellLog:*`).
- `OSDU_SEARCH_QUERY` — query string for search tests (default: `*`).
- `OSDU_SEARCH_LIMIT` — result limit for search tests (default: `5`).
- `OSDU_GROUP_TYPE` — group type filter for entitlements tests (default: `none`).

## Running Tests

Integration tests hit a real OSDU server. On first run a browser window will open for interactive MSAL login; the resulting token is cached in `.msal_token_cache.bin`.

```bash
# Run all tests
uv run pytest

# Unit tests only (no .env or network required)
uv run pytest tests/test_facade.py tests/test_transport.py tests/test_logging.py

# Single integration test by name
uv run pytest tests/entitlements_test.py::test_list_my_entitlement_groups

# Verbose output (print statements, debug logs)
uv run pytest -s
```

For tests that read env vars not loaded into the process environment by Pydantic Settings (e.g. `OSDU_MEMBER_EMAIL` consumed via `os.environ`), export them in your shell or prefix the command:

```bash
export OSDU_MEMBER_EMAIL=your.name@equinor.com
uv run pytest tests/entitlements_test.py
```
