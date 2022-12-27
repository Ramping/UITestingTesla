import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options as firefox_options


def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # use headless if you not need a browser UI
    # options.add_argument('headless')
    # options.add_argument('--start-maximized')
    options.add_argument('--kiosk-printing')
    # options.add_argument('--window-size=1366, 768')
    return options


def get_firefox_options():
    options = firefox_options()
    # options.add_argument('firefox')  # use headless if you not need a browser UI
    options.add_argument('headless')
    options.add_argument('--start-maximized')
    # options.add_argument('--window-size=1366, 768')
    return options


def pytest_addoption(parser):
    # parser.addoption('--env', action='store', default='dev')
    parser.addoption('--browser', action='store', default='chrome')


@pytest.fixture
def browser(request):
    browser = request.config.getoption('browser').lower()
    if browser not in ['chrome', 'firefox']:
        raise ValueError('--browser value mast be chrome or firefox')
    return browser


@pytest.fixture
def browser(request):
    browser = request.config.getoption('browser').lower()
    if browser not in ['chrome', 'firefox']:
        raise ValueError('--browser value mast be chrome or firefox')
    return browser


@pytest.fixture
def get_webdriver(browser):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=get_chrome_options()) if browser == 'chrome' else webdriver.Firefox(
        options=get_firefox_options())
    driver._browser = browser
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://www.tesla.com/'
    if request is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
