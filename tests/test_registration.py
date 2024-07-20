from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators
import urls


# сценарий регистрации с генерацией имени, почты, пароля
def test_registation(driver, name_generator, mail_generator, password_generator):
    # начали с формы регистрации
    driver.get(urls.reg_url)

    # ждем загрузки формы регистрации
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.locators_reg_form)))

    # убеждаемся что в форме есть 3 инпута для регистрации
    reg_form = driver.find_elements(By.CSS_SELECTOR, ".input__container")
    assert len(reg_form) == 3

    # генерируем имя
    name = name_generator
    driver.find_element(By.XPATH, locators.name_input).send_keys(name)

    value_name = driver.find_element(By.XPATH, locators.name_input).get_attribute('value')
    # проверяем что поле Имя заполнено
    assert name in value_name

    # генерируем почту
    email = mail_generator
    driver.find_element(By.XPATH, locators.reg_email_input).send_keys(email)

    # сохраняем значение
    value_email = driver.find_element(By.XPATH, locators.reg_email_input).get_attribute('value')

    # проверяем что почта заполнена
    assert email in value_email

    # генерируем пароль
    password = password_generator
    driver.find_element(By.XPATH, locators.reg_password_input).send_keys(password)

    # сохраняем значение
    value_password = driver.find_element(By.XPATH, locators.reg_password_input).get_attribute('value')

    # проверяем что поле пароль заполнено и оно больше или равно 6 символов
    assert password in value_password
    assert value_password >= '6'

    # Жемем кнопку Зарегистрироваться
    driver.find_element(By.XPATH, locators.locators_registr_button).click()

    # ожидаем форму с логином и паролем, при этом дожидаясь кнопки Войти
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.locators_button_enter)))

    # убедились что ссылка верная
    assert driver.current_url == urls.login_url

    # закрываем брайзер
    driver.quit()
