from src.tokens import validate


def test_token_requires_a_subject():
    assert not validate("demo-")


def test_token_with_subject_is_valid():
    assert validate("demo-user-123")
    assert not validate("production-user-123")
