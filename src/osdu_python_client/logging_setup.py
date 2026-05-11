from __future__ import annotations

import logging

_LIBRARY_LOGGER = "osdu_python_client"
_BODY_LOGGER = "osdu_python_client.transport.body"


def enable_debug_logging(
    level: int = logging.DEBUG,
    include_bodies: bool = False,
    handler: logging.Handler | None = None,
) -> None:
    """Convenience setup for local debugging.

    Sets the ``osdu_python_client`` logger to ``level`` and attaches a stream
    handler if none is present. With ``include_bodies=True``, also lifts the
    ``osdu_python_client.transport.body`` logger so request/response bodies
    are logged (truncated to ~2KB, ``Authorization`` and ``Cookie`` headers
    redacted).

    Production consumers should configure their own handlers and formatters
    via ``logging.config`` instead of calling this.
    """
    logger = logging.getLogger(_LIBRARY_LOGGER)
    logger.setLevel(level)
    if handler is not None:
        logger.addHandler(handler)
    elif not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
        h = logging.StreamHandler()
        h.setFormatter(logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s"))
        logger.addHandler(h)
    logging.getLogger(_BODY_LOGGER).setLevel(
        logging.DEBUG if include_bodies else logging.WARNING
    )
