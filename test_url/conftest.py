import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",   # хранит значение аргумента
        default="https://ya.ru/",
        help="This is request url"
    )
    parser.addoption(
        "--status_code",
        action="store",  # хранит значение аргумента
        default="200",
        help="This is response status code")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def status_code(request):
    return int(request.config.getoption("--status_code"))