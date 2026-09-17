"""Intentionally unsafe fixture used to demonstrate BuildPulse PR scanning.

The value below is synthetic and cannot authenticate to any service.
"""

DEMO_API_KEY = "sk-synthetic-buildpulse-demo-1234567890"


def configured_demo_key() -> str:
    return DEMO_API_KEY
