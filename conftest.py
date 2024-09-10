import pytest

def pytest_addoption(parser):
    parser.addoption("--api-key", action="store", default=None, help="API key for geoloc_util.py")

@pytest.fixture
def api_key(request):
    return request.config.getoption("--api-key")