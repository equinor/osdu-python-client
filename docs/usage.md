# Usage

Two layers are available:

1. **`osdu_python_client.OsduClient`** — recommended. A facade that handles auth, partition headers, retries with exponential backoff and `Retry-After`, a shared connection pool across all services, and ergonomic per-operation method dispatch.
2. **`osdu_python_client.generated.<service>.AuthenticatedClient`** — the raw generated clients. Use directly when you want to bring your own httpx setup.

## Recommended: `OsduClient`

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

Each `osdu.<service>.<operation>(...)` call:

- auto-binds the underlying generated client and `data-partition-id`
- returns the parsed response model on 2xx
- raises `OsduError` on non-2xx (the error message includes the server's response body — typed `AppError` if the spec defines one, raw JSON otherwise)

For the full `Response` envelope (status code, headers, raw parsed error model), call `.detailed`:

```python
result = osdu.search.query_records.detailed(body=request)
print(result.status_code, result.headers)
```

`osdu.<service>.raw` is the underlying `AuthenticatedClient` if you ever need it.

## Async

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

## Auth Providers

Auth is pluggable. `OsduConfig.auth_provider` (env var `AUTH_PROVIDER`) selects which CSP provider to use.

| Provider        | Status   | Required config                                         |
| --------------- | -------- | ------------------------------------------------------- |
| `azure_msal`    | built-in | `CLIENT_ID`, `AUTHORITY`, `SCOPES`, `AUTH_MODE`         |
| `aws_cognito`   | stub     | bring your own `TokenProvider` (see below)              |
| `gcp_iam`       | stub     | bring your own `TokenProvider`                          |
| `ibm_iam`       | stub     | bring your own `TokenProvider`                          |

### Azure (default)

`AzureMsalConfig.auth_mode` (env var `AUTH_MODE`) selects the MSAL flow. All three persist tokens to `msal_cache_path` (default `.msal_token_cache.bin`).

| MSAL flow              | When to use            | Required config                          |
| ---------------------- | ---------------------- | ---------------------------------------- |
| `interactive`          | Local dev / tests      | `client_id`, `authority`, `scopes`       |
| `device_flow`          | Headless ops scripts   | `client_id`, `authority`, `scopes`       |
| `client_credentials`   | CI, service-to-service | + `client_secret`                        |

```python
# Interactive (default)
osdu = OsduClient()
```

### Bring your own provider (any CSP)

Implement the `TokenProvider` Protocol (one method) and pass it to `OsduClient`. Works for AWS, GCP, IBM, custom auth, or anything else:

```python
class MyAwsProvider:
    def get_token(self, force_refresh: bool = False) -> str:
        # Cognito / IAM / whatever — return a bearer token string
        return "..."

osdu = OsduClient(token_provider=MyAwsProvider())
```

For shared provider implementations, register them so users can select via `AUTH_PROVIDER=...`:

```python
from osdu_python_client.auth import register_provider
register_provider("my_csp", lambda config: MyAwsProvider())
```

Tokens are injected per-request, so refresh after a 401 takes effect immediately. The transport retries 401 once with `force_refresh=True` and retries `429/502/503/504` with backoff honouring `Retry-After`.

## Per-service Header Overrides

Some endpoints accept extra headers (e.g. `frame-of-reference` on CRS). Use the `with_headers` context manager — it scopes mutations to one or all built service clients and restores them on exit.

```python
with osdu.with_headers(service="crs_conversion", **{"frame-of-reference": "units=SI"}):
    osdu.crs_conversion.convert_records(body=req)

# Or apply to every service client built so far (e.g. correlation IDs):
with osdu.with_headers(**{"x-correlation-id": correlation_id}):
    ...
```

The async client exposes the same helper as `async with osdu.with_headers(...)`.

## Debugging

The library logs through Python's standard `logging` module. Loggers used:

| Logger                                | Level   | What it emits                                                |
| ------------------------------------- | ------- | ------------------------------------------------------------ |
| `osdu_python_client.transport`        | DEBUG   | every request/response with method, URL, status, timing      |
| `osdu_python_client.transport`        | INFO    | retry decisions, 401 → token refresh                         |
| `osdu_python_client.transport`        | WARNING | retries exhausted                                            |
| `osdu_python_client.transport.body`   | DEBUG   | request/response bodies (truncated to ~2KB)                  |
| `osdu_python_client.auth`             | DEBUG   | token acquisition (cache hit / fresh, never the token value) |

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

## Low-level: Raw `AuthenticatedClient`

The generated clients can also be used directly with a static token (no retry, no auto-refresh, no shared connection pool):

```python
from osdu_python_client.generated.entitlements.api.list_group_on_behalf_of_api import (
    list_all_partition_groups,
)
from osdu_python_client.generated.entitlements.client import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://your-osdu-instance.com/api/entitlements/v2",
    token="YOUR_ACCESS_TOKEN",
)

result = list_all_partition_groups.sync_detailed(
    client=client,
    data_partition_id="your-partition-id",
    type_="NONE",
)
if result.parsed:
    for group in result.parsed.groups:
        print(group.name, group.email)
```

The async variant is `asyncio_detailed(...)`.
