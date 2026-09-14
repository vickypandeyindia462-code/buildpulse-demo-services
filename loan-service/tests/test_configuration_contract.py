"""Controlled BuildPulse failure: runtime pool capacity must match configuration."""

from src.config import CONNECTION_POOL_MAX
from src.connection_pool import MAX_CONNECTIONS


def test_connection_pool_matches_runtime_configuration():
    assert MAX_CONNECTIONS == CONNECTION_POOL_MAX, (
        f"connection pool configuration drift: runtime={MAX_CONNECTIONS}, configured={CONNECTION_POOL_MAX}"
    )
