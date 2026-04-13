import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginLocators, PersonalCabinetLocators

class TestPersonalCabinet:

    #  Переход в личный кабинет 
    def test_go_to_personal_cabinet(self, driver):
        driver.maximize_window()
        driver.get("https://stellarburgers.education-services.ru/login")
        
        wait = WebDriverWait(driver, 15)
        wait.until(EC.visibility_of_element_located(LoginLocators.EMAIL_INPUT)).send_keys("ksenia_kozyreva_43_127@yandex.ru")
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys("pass1234")
        driver.find_element(*LoginLocators.LOGIN_BUTTON_ON_LOGIN_PAGE).click()
        
        wait.until(EC.url_to_be("https://stellarburgers.education-services.ru/"))
        acc_btn = wait.until(EC.element_to_be_clickable(PersonalCabinetLocators.ACCOUNT_BUTTON))
        driver.execute_script("arguments[0].click();", acc_btn)
        
        wait.until(EC.url_contains("/account/profile"))
        assert "/account/profile" in driver.current_url
 

    #  Метод для логина 
    def login(self, driver, wait):
        driver.get("https://stellarburgers.education-services.ru/login")
        wait.until(EC.visibility_of_element_located(LoginLocators.EMAIL_INPUT)).send_keys("ksenia_kozyreva_43_127@yandex.ru")
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys("pass1234")
        driver.find_element(*LoginLocators.LOGIN_BUTTON_ON_LOGIN_PAGE).click()
        wait.until(EC.url_to_be("https://stellarburgers.education-services.ru/"))

    # Переход из личного кабинета в Конструктор
    def test_go_to_constructor_from_profile(self, driver):
        wait = WebDriverWait(driver, 15)
        self.login(driver, wait) 
        
        acc_btn = wait.until(EC.element_to_be_clickable(PersonalCabinetLocators.ACCOUNT_BUTTON))
        driver.execute_script("arguments[0].click();", acc_btn)
        wait.until(EC.url_contains("/account/profile"))
        
        const_btn = wait.until(EC.element_to_be_clickable(PersonalCabinetLocators.CONSTRUCTOR_BUTTON))
        driver.execute_script("arguments[0].click();", const_btn)
        
        wait.until(EC.url_to_be("https://stellarburgers.education-services.ru/"))
        assert driver.current_url == "https://stellarburgers.education-services.ru/"

    # Переход из личного кабинета по клику на Логотип
    def test_go_to_main_page_via_logo(self, driver):
        wait = WebDriverWait(driver, 15)
        self.login(driver, wait) 
        
        acc_btn = wait.until(EC.element_to_be_clickable(PersonalCabinetLocators.ACCOUNT_BUTTON))
        driver.execute_script("arguments[0].click();", acc_btn)
        wait.until(EC.url_contains("/account/profile"))
        
        logo_btn = wait.until(EC.element_to_be_clickable(PersonalCabinetLocators.LOGO))
        driver.execute_script("arguments[0].click();", logo_btn)
        
        wait.until(EC.url_to_be("https://stellarburgers.education-services.ru/"))
        assert driver.current_url == "https://stellarburgers.education-services.ru/"

        
        # Выход из аккаунта
    def test_logout_from_personal_cabinet(self, driver):
        driver.maximize_window()
        driver.get("https://stellarburgers.education-services.ru/login")
        wait = WebDriverWait(driver, 15)
        
        wait.until(EC.visibility_of_element_located(LoginLocators.EMAIL_INPUT)).send_keys("ksenia_kozyreva_43_127@yandex.ru")
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys("pass1234")
        driver.find_element(*LoginLocators.LOGIN_BUTTON_ON_LOGIN_PAGE).click()
        
        wait.until(EC.url_to_be("https://stellarburgers.education-services.ru/"))
        acc_btn = wait.until(EC.element_to_be_clickable(PersonalCabinetLocators.ACCOUNT_BUTTON))
        driver.execute_script("arguments[0].click();", acc_btn)
        
        logout_btn = wait.until(EC.presence_of_element_located(PersonalCabinetLocators.LOGOUT_BUTTON))
        driver.execute_script("arguments[0].click();", logout_btn)
        
        wait.until(EC.url_contains("/login"))
        assert "/login" in driver.current_url
