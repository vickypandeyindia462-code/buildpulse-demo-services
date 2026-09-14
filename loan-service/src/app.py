from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .connection_pool import MAX_CONNECTIONS, pool_is_saturated
from .domain import assess

app = FastAPI(title="BuildPulse Loan Service", version="24.3.0")


class Application(BaseModel):
    application_id: str = Field(min_length=3)
    credit_score: int
    annual_income: int
    requested_amount: int


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "loan-service", "pool_max": MAX_CONNECTIONS}


@app.post("/v1/loans/decisions")
def decide(request: Application) -> dict:
    try:
        return assess(**request.model_dump())
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@app.get("/internal/pool/{connections}")
def pool_status(connections: int) -> dict:
    return {"in_use": connections, "max": MAX_CONNECTIONS, "saturated": pool_is_saturated(connections)}
