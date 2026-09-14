from src.connection_pool import MAX_CONNECTIONS, pool_is_saturated


def test_pool_is_saturated_at_ninety_percent():
    assert pool_is_saturated(int(MAX_CONNECTIONS * 0.9))


def test_pool_is_not_saturated_below_threshold():
    assert not pool_is_saturated(int(MAX_CONNECTIONS * 0.89))
