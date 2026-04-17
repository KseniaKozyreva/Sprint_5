import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginLocators 

# Класс страницы
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def login_as_user(self, email, password):
        email_input = self.wait.until(EC.visibility_of_element_located(LoginLocators.EMAIL_INPUT))
        email_input.send_keys(email)
        self.driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)
        
        login_button = self.wait.until(EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON_ON_LOGIN_PAGE))
        self.driver.execute_script("arguments[0].click();", login_button)

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
    driver.get(f"{base_url}login")
    
    login_page = LoginPage(driver)
    login_page.login_as_user("ksenia_kozyreva_43_127@yandex.ru", "pass1234")
    
    WebDriverWait(driver, 15).until(EC.url_to_be(base_url))
    
    return driver  
