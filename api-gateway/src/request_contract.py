"""Gateway request validation and correlation propagation."""

import re
from uuid import uuid4

CORRELATION_PATTERN = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9._-]{2,63}$")


def correlation_id(value: str | None) -> str:
    if value and CORRELATION_PATTERN.fullmatch(value):
        return value
    return f"bp-{uuid4().hex[:16]}"


def upstream_headers(incoming: dict[str, str]) -> dict[str, str]:
    requested = incoming.get("x-correlation-id") or incoming.get("X-Correlation-ID")
    return {"X-Correlation-ID": correlation_id(requested)}
