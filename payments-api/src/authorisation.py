"""Synthetic payment-authorisation contract."""


def authorise(reservation_id: str, amount: int) -> dict:
    status = "rejected" if amount <= 0 else "authorised"
    return {"reservation_id": reservation_id, "amount": amount, "status": status}
