import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ConstructorLocators

class TestConstructor:


    # Вкладка Соусы
    def test_go_to_sauces_section(self, driver, base_url):
        driver.get(base_url)
        wait = WebDriverWait(driver, 15)
        
        tab = wait.until(EC.presence_of_element_located(ConstructorLocators.SAUCES_TAB))
        
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tab)
        driver.execute_script("arguments[0].click();", tab)
        
        wait.until(lambda d: "tab_type_current" in d.find_element(*ConstructorLocators.SAUCES_TAB).get_attribute("class"))
        
        assert "tab_type_current" in driver.find_element(*ConstructorLocators.SAUCES_TAB).get_attribute("class")

    # Вкладка Начинки
    def test_go_to_fillings_section(self, driver, base_url):
        driver.get(base_url)
        wait = WebDriverWait(driver, 15)
        
        tab = wait.until(EC.presence_of_element_located(ConstructorLocators.FILLINGS_TAB))
        
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tab)
        driver.execute_script("arguments[0].click();", tab)
        
        wait.until(lambda d: "tab_type_current" in d.find_element(*ConstructorLocators.FILLINGS_TAB).get_attribute("class"))
        
        assert "tab_type_current" in driver.find_element(*ConstructorLocators.FILLINGS_TAB).get_attribute("class")


    # Вкладка Булки
    def test_go_to_buns_section(self, driver, base_url):
        driver.get(base_url)
        wait = WebDriverWait(driver, 15)
        
        sauce_tab = wait.until(EC.presence_of_element_located(ConstructorLocators.SAUCES_TAB))
        driver.execute_script("arguments[0].click();", sauce_tab)
        wait.until(lambda d: "tab_type_current" in d.find_element(*ConstructorLocators.SAUCES_TAB).get_attribute("class"))
        
        buns_tab = wait.until(EC.presence_of_element_located(ConstructorLocators.BUNS_TAB))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", buns_tab)
        driver.execute_script("arguments[0].click();", buns_tab)
        
        wait.until(lambda d: "tab_type_current" in d.find_element(*ConstructorLocators.BUNS_TAB).get_attribute("class"))
        
        assert "tab_type_current" in driver.find_element(*ConstructorLocators.BUNS_TAB).get_attribute("class")
