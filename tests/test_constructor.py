import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ConstructorLocators

class TestConstructor:
    # Вкладка Соусы
    def test_go_to_sauces_section(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 10)
         
        sauce_tab = wait.until(EC.presence_of_element_located(ConstructorLocators.SAUCES_TAB))
        driver.execute_script("arguments[0].click();", sauce_tab)
        
        assert wait.until(EC.presence_of_element_located(ConstructorLocators.SAUCES_TAB))

    # Вкладка Начинки
    def test_go_to_fillings_section(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 10)
        
        filling_tab = wait.until(EC.presence_of_element_located(ConstructorLocators.FILLINGS_TAB))
        driver.execute_script("arguments[0].click();", filling_tab)
        
        assert wait.until(EC.presence_of_element_located(ConstructorLocators.FILLINGS_TAB))

    # Вкладка Булки 
    def test_go_to_buns_section(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 10)
        
        sauce_tab = wait.until(EC.presence_of_element_located(ConstructorLocators.SAUCES_TAB))
        driver.execute_script("arguments[0].click();", sauce_tab)
        wait.until(EC.presence_of_element_located(ConstructorLocators.SAUCES_TAB))
        
        buns_tab = wait.until(EC.presence_of_element_located(ConstructorLocators.BUNS_TAB))
        driver.execute_script("arguments[0].click();", buns_tab)
        
        assert wait.until(EC.presence_of_element_located(ConstructorLocators.BUNS_TAB))
