from src.tokens import validate


def test_empty_demo_token_is_rejected():
    assert not validate("demo-"), "token validator accepted a token without a subject"
