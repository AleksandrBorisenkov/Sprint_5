from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators
import urls


# проверили вывод ошибки длины пароля при регистрации
def test_registration_password_error(driver, name_generator, mail_generator, password_generator):
    # начали с формы регистрации
    driver.get(urls.reg_url)

    # ждем загрузки формы
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
    value_email = driver.find_element(By.XPATH, locators.reg_email_input).get_attribute('value')

    # проверяем что почта заполнена
    assert email in value_email

    # передаем пароль 5 символов
    password = '12345'
    driver.find_element(By.XPATH, locators.reg_password_input).send_keys(password)
    # сохраняем значение
    value_password = driver.find_element(By.XPATH, locators.reg_password_input).get_attribute('value')

    # проверяем что поле пароль заполнено
    assert password in value_password

    # Жемем кнопку Зарегистрироваться
    driver.find_element(By.XPATH, locators.locators_registr_button).click()

    # дожидаемся вывода ошибки
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.error_password)))

    # Сохраняем текст ошибки и сравниваем с эталонным
    error_password = driver.find_element(By.XPATH, locators.error_password).text
    assert error_password == 'Некорректный пароль'

    # закрываем брайзер
    driver.quit()
