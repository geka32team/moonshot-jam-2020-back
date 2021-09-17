import pytest


@pytest.mark.parametrize('endpoint,methods', (
    ('/api/register', {'POST'}),
    ('/api/signin', {'POST'}),
    ('/api/signout', {'POST'}),
))
def test_if_http_method_is_allowed(api_client_unauth, endpoint, methods):
    all_methods = {'GET', 'POST', 'PUT', 'DELETE', 'CONNECT', 'TRACE', 'PATCH'}
    for method in all_methods - methods:
        assert api_client_unauth.open(
            endpoint, method=method).status_code == 405
