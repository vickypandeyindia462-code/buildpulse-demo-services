"""Synthetic token-validation behaviour."""


def validate(token: str) -> bool:
    return token.startswith("demo-") and bool(token.removeprefix("demo-"))
