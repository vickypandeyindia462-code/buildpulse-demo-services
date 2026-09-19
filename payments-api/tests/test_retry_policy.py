from src.retry_policy import should_retry


def test_retryable_service_unavailable_is_retried():
    assert should_retry(503, 1)


def test_final_attempt_is_not_retried():
    assert not should_retry(503, 3)
