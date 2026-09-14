"""Synthetic connection-pool configuration used for risk demonstrations."""

MAX_CONNECTIONS = 40
ACQUIRE_TIMEOUT_SECONDS = 2.0
RETRY_LIMIT = 2


def pool_is_saturated(in_use_connections: int) -> bool:
    return in_use_connections / MAX_CONNECTIONS >= 0.90
