import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from locators import RegistrationLocators
from generators import generate_email

# Класс страницы
class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def register(self, name=None, email=None, password=None):
        if name:
            self.wait.until(EC.visibility_of_element_located(RegistrationLocators.NAME_INPUT)).send_keys(name)
        if email:
            self.driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
        if password:
            self.driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*RegistrationLocators.REG_BUTTON).click()

    def get_password_error(self):
        return self.wait.until(EC.visibility_of_element_located(RegistrationLocators.PASSWORD_ERROR)).text

    def get_login_header(self):
        return self.wait.until(EC.visibility_of_element_located(RegistrationLocators.LOGIN_HEADER))

class TestRegistration:

    # Успешная регистрация
    def test_successful_registration(self, driver, base_url):
        driver.get(f"{base_url}register")
        reg_page = RegistrationPage(driver) 
        
        reg_page.register("Ксения", generate_email(), "123456") 
        
        assert reg_page.get_login_header().is_displayed()

    # Ошибка при вводе короткого пароля (5 символов)
    def test_registration_error_short_password(self, driver, base_url):
        driver.get(f"{base_url}register")
        reg_page = RegistrationPage(driver)
        
        reg_page.register("Ксения", generate_email(), "12345")
        
        assert reg_page.get_password_error() == "Некорректный пароль"

    # Негативный тест: Пустое поле Имя 
    def test_registration_empty_name_error(self, driver, base_url):
        driver.get(f"{base_url}register")
        reg_page = RegistrationPage(driver)
        
        reg_page.register(name=None, email=generate_email(), password="123456")

        assert "/register" in driver.current_url
