import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import PersonalCabinetLocators

# Класс страницы 
class PersonalCabinetPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click_acc_btn(self):
        acc_btn = self.wait.until(EC.element_to_be_clickable(PersonalCabinetLocators.ACCOUNT_BUTTON))
        self.driver.execute_script("arguments[0].click();", acc_btn)

    def click_const_btn(self):
        const_btn = self.wait.until(EC.element_to_be_clickable(PersonalCabinetLocators.CONSTRUCTOR_BUTTON))
        self.driver.execute_script("arguments[0].click();", const_btn)

    def click_logo_btn(self):
        logo_btn = self.wait.until(EC.element_to_be_clickable(PersonalCabinetLocators.LOGO))
        self.driver.execute_script("arguments[0].click();", logo_btn)

    def click_logout_btn(self):
        logout_btn = self.wait.until(EC.element_to_be_clickable(PersonalCabinetLocators.LOGOUT_BUTTON))
        self.driver.execute_script("arguments[0].click();", logout_btn)

class TestPersonalCabinet:

    # Переход в личный кабинет 
    def test_go_to_personal_cabinet(self, driver, login_user, base_url):
        page = PersonalCabinetPage(driver)
        
        page.click_acc_btn()
        
        WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))
        assert "/account/profile" in driver.current_url

    # Переход из личного кабинета в Конструктор
    def test_go_to_constructor_from_profile(self, driver, login_user, base_url):
        page = PersonalCabinetPage(driver)
        
        page.click_acc_btn()
        WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))
        
        page.click_const_btn()
        
        WebDriverWait(driver, 10).until(EC.url_to_be(base_url))
        assert driver.current_url == base_url

    # Переход из личного кабинета по клику на Логотип
    def test_go_to_main_page_via_logo(self, driver, login_user, base_url):
        page = PersonalCabinetPage(driver)
        
        page.click_acc_btn()
        WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))
        
        page.click_logo_btn()
        
        WebDriverWait(driver, 10).until(EC.url_to_be(base_url))
        assert driver.current_url == base_url

    # Выход из аккаунта
    def test_logout_from_personal_cabinet(self, driver, login_user):
        page = PersonalCabinetPage(driver)
        
        page.click_acc_btn()
        page.click_logout_btn()
        
        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url
