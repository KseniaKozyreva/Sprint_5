import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginLocators

# Класс страницы 
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click_login_button(self):
        login_button = self.wait.until(EC.element_to_be_clickable(LoginLocators.MAIN_PAGE_LOGIN_BUTTON))
        self.driver.execute_script("arguments[0].click();", login_button)

    def click_acc_btn(self):
        acc_btn = self.wait.until(EC.element_to_be_clickable(LoginLocators.ACCOUNT_BUTTON))
        self.driver.execute_script("arguments[0].click();", acc_btn)

    def click_login_button_in_reg_form(self):
        login_button = self.wait.until(EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON_IN_REG_FORM))
        self.driver.execute_script("arguments[0].click();", login_button)

    def click_login_button_on_forgot_password_page(self):
        login_button = self.wait.until(EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON_ON_FORGOT_PASSWORD_PAGE))
        self.driver.execute_script("arguments[0].click();", login_button)

class TestLogin:
    # Вход через кнопку "Войти в аккаунт" 
    def test_login_from_main_page(self, driver, base_url):
        driver.get(base_url)
        page = LoginPage(driver)
        
        page.click_login_button()
        
        assert "/login" in driver.current_url

    # Вход через кнопку "Личный кабинет"
    def test_login_from_account_button(self, driver, base_url):
        driver.get(base_url)
        page = LoginPage(driver)
        
        page.click_acc_btn()

        assert "/login" in driver.current_url
        
    # Успешная проверка логина
    def test_successful_login(self, driver, login_user, base_url):
        assert driver.current_url == base_url

    # Вход через форму регистрации
    def test_login_from_registration_form(self, driver, base_url):
        driver.get(f"{base_url}register")
        page = LoginPage(driver)
        
        page.click_login_button_in_reg_form()

        assert "/login" in driver.current_url

    # Вход через форму восстановления пароля  
    def test_login_from_forgot_password_form(self, driver, base_url):
        driver.get(f"{base_url}forgot-password")
        page = LoginPage(driver)
        
        page.click_login_button_on_forgot_password_page()
        
        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url

