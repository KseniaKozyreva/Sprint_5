import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginLocators 

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Выберите браузер: chrome или firefox")

@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        try:
            service = FirefoxService(GeckoDriverManager().install())
            browser = webdriver.Firefox(service=service)
        except Exception:
            browser = webdriver.Firefox() 

    else:
        raise pytest.UsageError("--browser должен быть chrome или firefox")

    browser.maximize_window()
    yield browser
    browser.quit()

BASE_URL = "https://stellarburgers.education-services.ru/"

@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def login_user(driver, base_url): 
    wait = WebDriverWait(driver, 15)
    driver.get(f"{base_url}login")
    email_input = wait.until(EC.visibility_of_element_located(LoginLocators.EMAIL_INPUT))
    email_input.send_keys("ksenia_kozyreva_43_127@yandex.ru")
    
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys("pass1234")
    
    login_button = wait.until(EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON_ON_LOGIN_PAGE))
    driver.execute_script("arguments[0].click();", login_button)
    
    wait.until(EC.url_to_be(base_url))
    return wait
