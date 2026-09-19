from src.routing import ROUTES


def test_gateway_routes_core_services():
    assert ROUTES["/loans"] == "loan-service"
    assert ROUTES["/payments"] == "payments-api"
