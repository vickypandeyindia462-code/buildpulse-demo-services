from fastapi import FastAPI, Header, HTTPException

from .request_contract import correlation_id
from .routing import ROUTES

app = FastAPI(title="BuildPulse API Gateway", version="24.3.0")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "api-gateway", "routes": len(ROUTES)}


@app.get("/internal/routes/{route}")
def resolve(route: str, x_correlation_id: str | None = Header(default=None)) -> dict:
    path = f"/{route}"
    target = ROUTES.get(path)
    if target is None:
        raise HTTPException(status_code=404, detail="route not found")
    return {"path": path, "service": target, "correlation_id": correlation_id(x_correlation_id)}
