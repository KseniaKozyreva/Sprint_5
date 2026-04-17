from selenium.webdriver.common.by import By

class RegistrationLocators:
    # Поле имя 
    NAME_INPUT =(By.XPATH, "(//input[@name='name'])[1]")
    # Поле email
    EMAIL_INPUT =(By.XPATH, "(//input[@name='name'])[2]")
    # Поле ввода пароля
    PASSWORD_INPUT =(By.XPATH, "//input[@name='Пароль']")
    # Кнопка регистрации 
    REG_BUTTON =(By.XPATH, './/button[text()="Зарегистрироваться"]')
    # Заголовок вход 
    LOGIN_HEADER =(By.XPATH, './/h2[text()="Вход"]')
    # Кнопка войти
    LOGIN_BUTTON =(By.XPATH, './/button[text()="Войти"]')
    # неверный пароль
    PASSWORD_ERROR =(By.XPATH, '//p[@class="input__error text_type_main-default" and text()="Некорректный пароль"]')
    
class LoginLocators:

    # Поле email
    EMAIL_INPUT =(By.CSS_SELECTOR, "input[name='name']")
    # Поле ввода пароля
    PASSWORD_INPUT =(By.NAME, "Пароль")
    # Кнопка Войти в аккаунт на главной странице
    MAIN_PAGE_LOGIN_BUTTON =(By.XPATH, "//button[text()='Войти в аккаунт']")
    # Кнопка Личный кабинет
    ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']/parent::a")
    # Кнопка Войти в личном кабинете
    LOGIN_BUTTON_ON_LOGIN_PAGE =(By.XPATH, "//form[contains(@class, 'Auth_form')]//button")
    # Ссылка Зарегистрироваться на странице входа
    REGISTRATION_LINK =(By.XPATH, '//a[contains(@class, "Auth_link_1fOlj") and contains(text(), "Зарегистрироваться")]')
    # Ссылка Войти в форме регистрации
    LOGIN_BUTTON_IN_REG_FORM =(By.LINK_TEXT, "Войти")
    # Ссылка на страницу восстановление пароля
    FORGOT_PASSWORD_LINK =(By.XPATH, '//a[contains(@class, "Auth_link_1fOlj") and contains(text(), "Восстановить пароль")]')
    # Ссылка Войти на странице востановления пароля
    LOGIN_BUTTON_ON_FORGOT_PASSWORD_PAGE = (By.LINK_TEXT, "Войти")
    

class PersonalCabinetLocators:
    # Кнопка коструктор
    CONSTRUCTOR_BUTTON =(By.XPATH, '//p[text()="Конструктор"]')
    # Кнопка Личный кабинет
    ACCOUNT_BUTTON =(By.XPATH, '//p[text()="Личный Кабинет"]')
    # Кнопка Логотип Stellar Burgers
    LOGO =(By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]/a")
    # Кнопка «Выход»
    LOGOUT_BUTTON =(By.XPATH, '//button[text()="Выход"]')



class ConstructorLocators:
    # вкладка «Булки»
    BUNS_TAB =(By.XPATH, '//span[text()="Булки"]/parent::div')
    # вкладка «Соусы»
    SAUCES_TAB =(By.XPATH, '//span[text()="Соусы"]/parent::div')
    # вкладка «Начинки»
    FILLINGS_TAB =(By.XPATH, '//span[text()="Начинки"]/parent::div') 
