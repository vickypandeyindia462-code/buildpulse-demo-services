from src.request_contract import correlation_id, upstream_headers


def test_valid_correlation_id_is_preserved():
    assert correlation_id("loan-request-123") == "loan-request-123"


def test_invalid_id_is_replaced():
    generated = correlation_id("bad id")
    assert generated.startswith("bp-")


def test_header_is_propagated():
    assert upstream_headers({"x-correlation-id": "trace-456"}) == {"X-Correlation-ID": "trace-456"}
