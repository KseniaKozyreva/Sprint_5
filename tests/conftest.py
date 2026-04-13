import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Выберите браузер: chrome или firefox")

@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("browser")
    
    if browser_name == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        browser = webdriver.Firefox(service=service)
    else:
        raise pytest.UsageError("--browser должен быть chrome или firefox")

    browser.maximize_window()
    yield browser
    browser.quit()
