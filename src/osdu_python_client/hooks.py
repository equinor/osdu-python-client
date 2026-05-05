from __future__ import annotations

from typing import Awaitable, Callable

import httpx


def partition_hook(data_partition_id: str) -> Callable[[httpx.Request], None]:
    def _hook(request: httpx.Request) -> None:
        request.headers.setdefault("data-partition-id", data_partition_id)

    return _hook


def async_partition_hook(
    data_partition_id: str,
) -> Callable[[httpx.Request], Awaitable[None]]:
    async def _hook(request: httpx.Request) -> None:
        request.headers.setdefault("data-partition-id", data_partition_id)

    return _hook
