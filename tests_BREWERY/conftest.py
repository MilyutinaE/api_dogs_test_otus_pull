import pytest


@pytest.fixture(scope="session")
def base_url():
    return "https://api.openbrewerydb.org/v1/breweries"