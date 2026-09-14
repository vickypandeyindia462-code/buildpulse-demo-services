import pytest

from src.claims import sign_claims, verify_claims


def test_signed_claims_round_trip():
    token = sign_claims({"sub": "demo-user", "exp": 200}, "secret")
    assert verify_claims(token, "secret", now=100)["sub"] == "demo-user"


def test_expired_claims_are_rejected():
    token = sign_claims({"sub": "demo-user", "exp": 100}, "secret")
    with pytest.raises(ValueError, match="expired"):
        verify_claims(token, "secret", now=100)


def test_modified_token_is_rejected():
    token = sign_claims({"sub": "demo-user", "exp": 200}, "secret")
    with pytest.raises(ValueError, match="signature"):
        verify_claims(token.replace("demo-user", "attacker"), "secret", now=100)
