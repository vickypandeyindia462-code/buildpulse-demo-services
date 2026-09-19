from src.authorisation import authorise


def test_non_positive_payment_is_rejected():
    result = authorise("res-invalid", 0)
    assert result["status"] == "rejected", "payment contract accepted a zero-value reservation"
