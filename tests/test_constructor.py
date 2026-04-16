import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ConstructorLocators

# Класс для конструктора
class ConstructorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click_tab(self, locator):
        tab = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tab)
        self.driver.execute_script("arguments[0].click();", tab)
        self.wait.until(lambda d: "tab_type_current" in d.find_element(*locator).get_attribute("class"))

    def is_tab_active(self, locator):
        try:
            self.wait.until(lambda d: "tab_type_current" in d.find_element(*locator).get_attribute("class"))
            return True
        except:
            return False

class TestConstructor:

    # Вкладка Соусы
    def test_go_to_sauces_section(self, driver, base_url):
        driver.get(base_url)
        page = ConstructorPage(driver)
        
        page.click_tab(ConstructorLocators.SAUCES_TAB)
        
        assert page.is_tab_active(ConstructorLocators.SAUCES_TAB)

    # Вкладка Начинки
    def test_go_to_fillings_section(self, driver, base_url):
        driver.get(base_url)
        page = ConstructorPage(driver)
        
        page.click_tab(ConstructorLocators.FILLINGS_TAB)
        
        assert page.is_tab_active(ConstructorLocators.FILLINGS_TAB)

    # Вкладка Булки
    def test_go_to_buns_section(self, driver, base_url):
        driver.get(base_url)
        page = ConstructorPage(driver)
        
        page.click_tab(ConstructorLocators.SAUCES_TAB)
        page.click_tab(ConstructorLocators.BUNS_TAB)
        
        assert page.is_tab_active(ConstructorLocators.BUNS_TAB)
