import parser
import pytest
from selenium import webdriver
from source.utilities.webdriver_factory import WebDriverFactory


@pytest.yield_fixture()
def setUp():
    print("Login to page")
    yield
    print("Logout of page")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    print("Close the browser")
    #driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", help="to run on different browser")
    parser.addoption("--osType", help="type of OS")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
