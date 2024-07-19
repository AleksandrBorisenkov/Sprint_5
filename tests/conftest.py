import random
import pytest

from selenium import webdriver


# сгенерирровали почту
@pytest.fixture
def mail_generator():
    letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    name = ''.join(random.choice(letters) for i in range(10))
    domain = ''.join(random.choice(letters) for i in range(6))
    country = ['ru', 'com', 'org', 'by', 'mail', 'rus', 'net', 'uk', 'us']
    mail = name + '@' + domain + '.' + random.choice(country)
    return mail


# сгенерировали пароль
@pytest.fixture
def password_generator():
    ls = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    password = ''.join(random.choice(ls) for i in range(10))
    return password


# сгенерировали имя и фамилию
@pytest.fixture
def name_generator():
    letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    frs_name = ''.join(random.choice(letters) for i in range(10))
    lst_name = ''.join(random.choice(letters) for i in range(10))
    return f"{frs_name} {lst_name}"


# предзаполнение формы логина и пароля
@pytest.fixture
def pre_email():
    pre_email = 'AleksandrBorisenkov11666@yandex.ru'
    return pre_email


@pytest.fixture
def pre_password():
    pre_password = 'QWERTY!@#'
    return pre_password


# настройка драйвера браузера
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture
def main_url():
    main_url = 'https://stellarburgers.nomoreparties.site/'
    return main_url


@pytest.fixture
def reg_url():
    reg_url = 'https://stellarburgers.nomoreparties.site/register'
    return reg_url


@pytest.fixture
def profile_url():
    profile_url = 'https://stellarburgers.nomoreparties.site/account/profile'
    return profile_url


@pytest.fixture
def login_url():
    login_url = 'https://stellarburgers.nomoreparties.site/login'
    return login_url


@pytest.fixture
def forgot_pas_url():
    forgot_pas_url = 'https://stellarburgers.nomoreparties.site/forgot-password'
    return forgot_pas_url


@pytest.fixture
def reset_pas_url():
    reset_pas_url = 'https://stellarburgers.nomoreparties.site/reset-password'
    return reset_pas_url


@pytest.fixture
def locators_souces():
    souces = "//*[@id='root']/div/main/section[1]/div[2]/h2[2][text()='Соусы']"
    return souces


@pytest.fixture
def locators_burger_section():
    burger_section = ".BurgerIngredients_ingredients__1N8v2"
    return burger_section


@pytest.fixture
def locators_bun():
    bun = "//*[@id='root']/div/main/section[1]/div[2]/h2[1][text()='Булки']"
    return bun


@pytest.fixture
def locators_ingredients():
    ingredients = "//*[@id='root']/div/main/section[1]/div[2]/h2[3][text()='Начинки']"
    return ingredients


@pytest.fixture
def locators_button_enter_account():
    button_enter_account = "//*[@id='root']/div/main/section[2]/div/button[text()='Войти в аккаунт']"
    return button_enter_account


@pytest.fixture
def locators_header_personal_account():
    header_personal_account = "//*[@id='root']/div/header/nav/a/p[text()='Личный Кабинет']"
    return header_personal_account


@pytest.fixture
def locators_button_enter():
    button_enter = ".//button[contains(text(),'Войти')]"
    return button_enter


@pytest.fixture
def locators_constructor_icon():
    constructor_icon = "//*[@id='root']/div/header/nav/ul/li[1]/a/p[text()='Конструктор']"
    return constructor_icon


@pytest.fixture
def name_input():
    name_input = "//form/fieldset[1]/div/div/input"
    return name_input


@pytest.fixture
def reg_email_input():
    reg_email_input = "//form/fieldset[2]/div/div/input"
    return reg_email_input


@pytest.fixture
def reg_password_input():
    reg_password_input = "//form/fieldset[3]/div/div/input"
    return reg_password_input

@pytest.fixture
def email_input():
    email_input = ".//input[@type='text']"
    return email_input


@pytest.fixture
def password_input():
    password_input = ".//input[@type='password']"
    return password_input


@pytest.fixture
def locators_create_order():
    create_order = "//*[@id='root']/div/main/section[2]/div/button[text()='Оформить заказ']"
    return create_order


@pytest.fixture
def locators_button_save():
    button_save = ".//button[2][text()='Сохранить']"
    return button_save


@pytest.fixture
def locators_reg_form():
    reg_form = "//*[@id='root']/div/main/div/form"
    return reg_form


@pytest.fixture
def locators_registr_button():
    registr_button = "//*[@id='root']/div/main/div/form/button[text()='Зарегистрироваться']"
    return registr_button


@pytest.fixture
def main_header():
    main_header = "//*[@id='root']/div/main/div/nav"
    return main_header


@pytest.fixture
def enter_link():
    enter_link = "//*[@id='root']/div/main/div/div/p/a[text()='Войти']"
    return enter_link


@pytest.fixture
def locator_allready_reg():
    allready_reg = "//*[@id='root']/div/main/div/div/p"
    return allready_reg


@pytest.fixture
def locators_logout_button():
    logout_button = "//*[@id='root']/div/main/div/nav/ul/li[3]/button[text()='Выход']"
    return logout_button


@pytest.fixture
def error_password():
    error_password = "//*[@id='root']/div/main/div/form/fieldset[3]/div/p"
    return error_password


@pytest.fixture
def main_logo():
    main_logo = "//*[@id='root']/div/header/nav/div"
    return main_logo
