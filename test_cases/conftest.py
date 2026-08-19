import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Select which browser to use")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser")
    return driver

###########for pytest html reports ###########
#hook for adding environment info in html report
def pytest_configure(config):
   config.stash[metadata_key] ['Project Name'] = 'Ecommerce Project, nopcommerce'
   config.stash[metadata_key]['Test Module Name'] = 'Admin Login Tests'
   config.stash[metadata_key]['Tester Name'] = 'Marcus Hannah'

#hook for delete/modify environment info in html report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
   #metadata.pop('JAVA_HOME',None)
   metadata.pop('Plugins', None)