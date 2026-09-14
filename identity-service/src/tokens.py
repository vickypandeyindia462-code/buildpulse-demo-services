"""Synthetic token-validation behaviour."""


def validate(token: str) -> bool:
    """Accept a demo token only when it includes a non-empty subject."""
    if not token.startswith("demo-"):
        return False
    subject = token.removeprefix("demo-").strip()
    return bool(subject)
