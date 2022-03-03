import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--lang', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    user_lang = request.config.getoption("lang")
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", user_lang)
    browser = webdriver.Firefox(firefox_profile=fp)
    return browser
