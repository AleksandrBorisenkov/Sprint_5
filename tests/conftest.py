import random

import pytest


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
@pytest.fixture(scope='session')
def email_and_password():
    pre_email = 'AleksandrBorisenkov11666@yandex.ru'
    pre_password = 'QWERTY!@#'
    return pre_email, pre_password
