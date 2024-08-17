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


