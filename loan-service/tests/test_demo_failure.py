from src.config import CONNECTION_POOL_MAX
from src.connection_pool import MAX_CONNECTIONS


def test_runtime_pool_matches_declared_configuration():
    assert MAX_CONNECTIONS == CONNECTION_POOL_MAX, (
        f"configuration drift: runtime={MAX_CONNECTIONS}, configured={CONNECTION_POOL_MAX}")
