import pytest

from src.domain import assess


def test_low_risk_application_is_approved():
    result = assess("app-100", 760, 120_000, 25_000)
    assert result["status"] == "approved"
    assert result["annual_rate"] == "7.25"


def test_high_amount_is_referred_with_explainable_reason():
    result = assess("app-101", 710, 80_000, 50_000)
    assert result["status"] == "referred"
    assert "amount-to-income-above-policy" in result["reasons"]


def test_invalid_score_is_rejected():
    with pytest.raises(ValueError, match="credit_score"):
        assess("app-102", 900, 80_000, 20_000)
