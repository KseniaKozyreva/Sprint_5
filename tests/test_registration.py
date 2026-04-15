import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from locators import RegistrationLocators
from generators import generate_email

class TestRegistration:

    # Успешная регистрация
    def test_successful_registration(self, driver, base_url):
        driver.get(f"{base_url}register")
        wait = WebDriverWait(driver, 10)

    
        wait.until(EC.visibility_of_element_located(RegistrationLocators.NAME_INPUT)).send_keys("Ксения")
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*RegistrationLocators.REG_BUTTON).click()

        login_header = wait.until(EC.visibility_of_element_located(RegistrationLocators.LOGIN_HEADER))
        assert login_header.is_displayed()
        

    # Ошибка при вводе короткого пароля (5 символов)
    def test_registration_error_short_password(self, driver, base_url):
        driver.get(f"{base_url}register")
        wait = WebDriverWait(driver, 10)

        wait.until(EC.visibility_of_element_located(RegistrationLocators.NAME_INPUT)).send_keys("Ксения")
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys("12345")
        driver.find_element(*RegistrationLocators.REG_BUTTON).click()

        error = wait.until(EC.visibility_of_element_located(RegistrationLocators.PASSWORD_ERROR))
        assert error.text == "Некорректный пароль" # Можно проверить и текст ошибки для надежности


    # Негативный тест: Пустое поле Имя 
    def test_registration_empty_name_error(self, driver, base_url):
        driver.get(f"{base_url}register")
        wait = WebDriverWait(driver, 10)

        wait.until(EC.visibility_of_element_located(RegistrationLocators.EMAIL_INPUT)).send_keys(generate_email())
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*RegistrationLocators.REG_BUTTON).click()

        assert "/register" in driver.current_url
