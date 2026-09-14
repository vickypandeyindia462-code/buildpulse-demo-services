import pytest

from src.ledger import ReservationLedger


def test_repeated_request_returns_same_reservation():
    ledger = ReservationLedger()
    first = ledger.reserve("key-1", "acct-1", 12500, "inr")
    second = ledger.reserve("key-1", "acct-1", 12500, "inr")
    assert first == second


def test_key_cannot_be_reused_for_a_different_payment():
    ledger = ReservationLedger()
    ledger.reserve("key-1", "acct-1", 12500, "INR")
    with pytest.raises(ValueError, match="different request"):
        ledger.reserve("key-1", "acct-1", 13000, "INR")
