"""HMAC-signed, short-lived demo token contract. Not a production identity system."""

import hashlib
import hmac
import json
import time


def sign_claims(claims: dict, secret: str) -> str:
    payload = json.dumps(claims, separators=(",", ":"), sort_keys=True)
    signature = hmac.new(secret.encode(), payload.encode(), hashlib.sha256).hexdigest()
    return f"{payload}.{signature}"


def verify_claims(token: str, secret: str, now: int | None = None) -> dict:
    try:
        payload, signature = token.rsplit(".", 1)
        claims = json.loads(payload)
    except (ValueError, json.JSONDecodeError) as exc:
        raise ValueError("malformed token") from exc
    expected = hmac.new(secret.encode(), payload.encode(), hashlib.sha256).hexdigest()
    if not hmac.compare_digest(signature, expected):
        raise ValueError("invalid signature")
    if int(claims.get("exp", 0)) <= (now if now is not None else int(time.time())):
        raise ValueError("expired token")
    return claims
