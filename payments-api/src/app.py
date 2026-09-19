from dataclasses import asdict

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

from .ledger import ReservationLedger

app = FastAPI(title="BuildPulse Payments API", version="24.3.0")
ledger = ReservationLedger()


class PaymentRequest(BaseModel):
    account_id: str
    amount_minor: int
    currency: str = "INR"


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "payments-api"}


@app.post("/v1/reservations")
def reserve(request: PaymentRequest, idempotency_key: str = Header(alias="Idempotency-Key")) -> dict:
    try:
        return asdict(ledger.reserve(idempotency_key, **request.model_dump()))
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc
