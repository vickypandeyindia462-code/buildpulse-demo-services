"""Loan application rules for the synthetic BuildPulse demo."""

from dataclasses import asdict, dataclass
from decimal import Decimal


@dataclass(frozen=True)
class LoanDecision:
    application_id: str
    status: str
    annual_rate: Decimal | None
    reasons: tuple[str, ...]


def assess(application_id: str, credit_score: int, annual_income: int, requested_amount: int) -> dict:
    reasons: list[str] = []
    if not 300 <= credit_score <= 850:
        raise ValueError("credit_score must be between 300 and 850")
    if annual_income <= 0 or requested_amount <= 0:
        raise ValueError("income and requested amount must be positive")
    if credit_score < 620:
        reasons.append("credit-score-below-policy")
    if requested_amount > annual_income * 0.45:
        reasons.append("amount-to-income-above-policy")
    approved = not reasons
    decision = LoanDecision(
        application_id=application_id,
        status="approved" if approved else "referred",
        annual_rate=Decimal("7.25") if approved else None,
        reasons=tuple(reasons),
    )
    result = asdict(decision)
    result["annual_rate"] = str(decision.annual_rate) if decision.annual_rate else None
    result["reasons"] = list(decision.reasons)
    return result
