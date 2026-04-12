import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginLocators


class TestLogin:
    # Вход через кнопку Вход в аккаунт на главной странице
    def test_login_from_main_page(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginLocators.MAIN_PAGE_LOGIN_BUTTON)
        )
        
        driver.execute_script("arguments[0].click();", login_button)
        
        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        assert driver.current_url == "https://stellarburgers.education-services.ru/login"


    # Вход через кнопку Личный кабинет 
    def test_login_from_account_button(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")

        wait = WebDriverWait(driver, 10)
    
        element = wait.until(EC.visibility_of_element_located(LoginLocators.ACCOUNT_BUTTON))
        wait.until(EC.element_to_be_clickable(LoginLocators.ACCOUNT_BUTTON))
    
        element.click()

        wait.until(EC.url_contains("/login"))
        assert "/login" in driver.current_url


    # Вход через кнопку Войти в форме регистрации
    def test_login_from_registration_form(self, driver):
        driver.maximize_window()
        driver.get("https://stellarburgers.education-services.ru/register")
        
        wait = WebDriverWait(driver, 15)
        login_link = wait.until(EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON_IN_REG_FORM))
        
        login_link.click()
        
        wait.until(EC.visibility_of_element_located(LoginLocators.EMAIL_INPUT)).send_keys("ksenia_kozyreva_43_127@yandex.ru")
        
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys("pass1234")
        
        wait.until(EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON_ON_LOGIN_PAGE)).click()

        wait.until(EC.url_to_be("https://stellarburgers.education-services.ru/"))
        assert driver.current_url == "https://stellarburgers.education-services.ru/"



    # Вход через кнопку Войти в форме восстановления пароля 
    def test_login_from_forgot_password_form(self, driver):
        driver.get("https://stellarburgers.education-services.ru/forgot-password")
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON_ON_FORGOT_PASSWORD_PAGE)
        ).click()
        
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys("ksenia_kozyreva_43_127@yandex.ru")
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys("pass1234")
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON_ON_LOGIN_PAGE)
        ).click()

        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))
        assert driver.current_url == "https://stellarburgers.education-services.ru/"
