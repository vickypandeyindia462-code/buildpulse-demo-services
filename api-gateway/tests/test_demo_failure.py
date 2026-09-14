from src.routing import ROUTES


def test_identity_route_is_registered():
    assert ROUTES["/identity"] == "identity-service"
