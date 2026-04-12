import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from locators import RegistrationLocators
from generators import generate_email

class TestRegistration:


    # Успешная регистрация
    def test_successful_registration(self, driver):
        driver.get("https://stellarburgers.education-services.ru/register")

        driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys("Ксения")
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*RegistrationLocators.REG_BUTTON).click()

        error_msg = WebDriverWait(driver, 10).until( EC.visibility_of_element_located(RegistrationLocators.LOGIN_HEADER))
        assert error_msg.is_displayed()
        

    # Ошибка при вводе 5 символов в поле пароль
    def test_registration_error_short_password(self, driver):
        driver.get("https://stellarburgers.education-services.ru/register")

        driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys("Ксения")
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys("12345")
        driver.find_element(*RegistrationLocators.REG_BUTTON).click()

        error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.PASSWORD_ERROR))
        assert error.is_displayed()   


    # Негативный тест: Пустое поле Имя 
    def test_registration_empty_name_error(self, driver):
        driver.get("https://stellarburgers.education-services.ru/register")


        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*RegistrationLocators.REG_BUTTON).click()

        assert "register" in driver.current_url
