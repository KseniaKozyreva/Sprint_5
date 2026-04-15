import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import PersonalCabinetLocators

class TestPersonalCabinet:

    # Переход в личный кабинет 
    def test_go_to_personal_cabinet(self, driver, login_user, base_url):
        wait = login_user 
        
        acc_btn = wait.until(EC.element_to_be_clickable(PersonalCabinetLocators.ACCOUNT_BUTTON))
        driver.execute_script("arguments[0].click();", acc_btn)
        
        wait.until(EC.url_contains("/account/profile"))
        assert "/account/profile" in driver.current_url

    # Переход из личного кабинета в Конструктор
    def test_go_to_constructor_from_profile(self, driver, login_user, base_url):
        wait = login_user
        
        driver.execute_script("arguments[0].click();", wait.until(EC.element_to_be_clickable(PersonalCabinetLocators.ACCOUNT_BUTTON)))
        wait.until(EC.url_contains("/account/profile"))
        
        const_btn = wait.until(EC.element_to_be_clickable(PersonalCabinetLocators.CONSTRUCTOR_BUTTON))
        driver.execute_script("arguments[0].click();", const_btn)
        
        wait.until(EC.url_to_be(base_url))
        assert driver.current_url == base_url

    #  Переход из личного кабинета по клику на Логотип
    def test_go_to_main_page_via_logo(self, driver, login_user, base_url):
        wait = login_user
        
        driver.execute_script("arguments[0].click();", wait.until(EC.element_to_be_clickable(PersonalCabinetLocators.ACCOUNT_BUTTON)))
        wait.until(EC.url_contains("/account/profile"))
        
        logo_btn = wait.until(EC.element_to_be_clickable(PersonalCabinetLocators.LOGO))
        driver.execute_script("arguments[0].click();", logo_btn)
        
        wait.until(EC.url_to_be(base_url))
        assert driver.current_url == base_url

    # Выход из аккаунта
    def test_logout_from_personal_cabinet(self, driver, login_user):
        wait = login_user
        
        driver.execute_script("arguments[0].click();", wait.until(EC.element_to_be_clickable(PersonalCabinetLocators.ACCOUNT_BUTTON)))
        
        logout_btn = wait.until(EC.element_to_be_clickable(PersonalCabinetLocators.LOGOUT_BUTTON))
        driver.execute_script("arguments[0].click();", logout_btn)
        
        wait.until(EC.url_contains("/login"))
        assert "/login" in driver.current_url
