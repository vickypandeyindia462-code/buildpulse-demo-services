"""Synthetic gateway contract checks."""

CORRELATION_HEADER = "X-Correlation-Id"


def has_correlation_id(headers: dict[str, str]) -> bool:
    return bool(headers.get(CORRELATION_HEADER))
