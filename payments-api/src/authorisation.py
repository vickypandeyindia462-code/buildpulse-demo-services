"""Synthetic payment-authorisation contract."""


def authorise(reservation_id: str, amount: int) -> dict:
    return {"reservation_id": reservation_id, "amount": amount, "status": "authorised"}
