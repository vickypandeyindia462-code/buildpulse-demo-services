"""Synthetic retry policy for idempotent payment reservations."""

MAX_ATTEMPTS = 3
RETRYABLE_STATUS_CODES = {429, 503, 504}


def should_retry(status_code: int, attempt: int) -> bool:
    return status_code in RETRYABLE_STATUS_CODES and attempt < MAX_ATTEMPTS
