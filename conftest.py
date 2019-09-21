from fixture.application import Application
import pytest

fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    local_url = request.config.getoption("--localUrl")
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    local_group_url = request.config.getoption("--localGroupUrl")
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url, username=username, password=password, local_url=local_url, local_group_url = local_group_url)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url, username=username, password=password, local_url=local_url, local_group_url = local_group_url)
    fixture.session.ensure_login(username=username, password=password)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
    parser.addoption("--localUrl", action="store", default="/addressbook/")
    parser.addoption("--localGroupUrl", action="store", default="/group.php")
    parser.addoption("--username", action="store", default="admin")
    parser.addoption("--password", action="store", default="secret")