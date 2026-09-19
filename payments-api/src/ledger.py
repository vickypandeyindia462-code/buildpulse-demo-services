"""In-memory idempotent reservation ledger for a deterministic demo."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Reservation:
    reservation_id: str
    account_id: str
    amount_minor: int
    currency: str
    status: str = "authorised"


class ReservationLedger:
    def __init__(self) -> None:
        self._by_key: dict[str, Reservation] = {}

    def reserve(self, idempotency_key: str, account_id: str, amount_minor: int, currency: str) -> Reservation:
        if not idempotency_key:
            raise ValueError("idempotency key is required")
        if amount_minor <= 0:
            raise ValueError("amount_minor must be positive")
        existing = self._by_key.get(idempotency_key)
        proposed = Reservation(f"res-{len(self._by_key) + 1:04d}", account_id, amount_minor, currency.upper())
        if existing and (existing.account_id, existing.amount_minor, existing.currency) != (
            proposed.account_id,
            proposed.amount_minor,
            proposed.currency,
        ):
            raise ValueError("idempotency key reused with different request")
        if existing:
            return existing
        self._by_key[idempotency_key] = proposed
        return proposed
