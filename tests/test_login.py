import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginLocators

class TestLogin:
    #  Вход через кнопку "Войти в аккаунт" 
    def test_login_from_main_page(self, driver, base_url):
        driver.get(base_url)
        
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginLocators.MAIN_PAGE_LOGIN_BUTTON)
        )
        driver.execute_script("arguments[0].click();", login_button)
        
        assert "/login" in driver.current_url

    # Вход через кнопку "Личный кабинет"
    def test_login_from_account_button(self, driver, base_url):
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)
        
        acc_btn = wait.until(EC.element_to_be_clickable(LoginLocators.ACCOUNT_BUTTON))
        driver.execute_script("arguments[0].click();", acc_btn)
        

    # Успешная проверка логина
    def test_successful_login(self, driver, login_user, base_url):
    
        assert driver.current_url == base_url

    # Вход через форму регистрации
    def test_login_from_registration_form(self, driver, base_url):
        driver.get(f"{base_url}register")
        
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON_IN_REG_FORM)
        )
        driver.execute_script("arguments[0].click();", login_button)

        assert "/login" in driver.current_url

    # Вход через форму восстановления пароля  
    def test_login_from_forgot_password_form(self, driver, base_url):
        driver.get(f"{base_url}forgot-password")
        wait = WebDriverWait(driver, 15)
        
        login_button = wait.until(
            EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON_ON_FORGOT_PASSWORD_PAGE)
        )
        
        driver.execute_script("arguments[0].click();", login_button)
        
        wait.until(EC.url_contains("/login"))
        assert "/login" in driver.current_url
