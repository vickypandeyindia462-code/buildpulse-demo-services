import os
import time

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .claims import sign_claims, verify_claims

app = FastAPI(title="BuildPulse Identity Service", version="24.3.0")
DEMO_SECRET = os.getenv("IDENTITY_DEMO_SECRET", "local-demo-only-change-me")


class TokenRequest(BaseModel):
    subject: str
    scopes: list[str] = []


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "identity-service"}


@app.post("/v1/tokens")
def issue(request: TokenRequest) -> dict:
    claims = {"sub": request.subject, "scopes": request.scopes, "exp": int(time.time()) + 900}
    return {"access_token": sign_claims(claims, DEMO_SECRET), "expires_in": 900}


@app.post("/v1/tokens/verify")
def verify(token: str) -> dict:
    try:
        return verify_claims(token, DEMO_SECRET)
    except ValueError as exc:
        raise HTTPException(status_code=401, detail=str(exc)) from exc
