from src.request_contract import has_correlation_id


def test_request_with_correlation_id_is_valid():
    assert has_correlation_id({"X-Correlation-Id": "demo-123"})


def test_request_without_correlation_id_is_invalid():
    assert not has_correlation_id({})
