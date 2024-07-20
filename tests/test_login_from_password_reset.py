from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators
import urls


def test_login_from_password_reset(driver, pre_email, pre_password):

    # начинаем с формы сброса пароля
    driver.get(urls.reset_pas_url)

    # ждем появление линка "Войти"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.enter_link)))

    # жмем по линку Войти
    driver.find_element(By.XPATH, locators.enter_link).click()

    # ждем загрузки формы с лоигном и паролем
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.locators_reg_form)))

    # проверяем что вышли на страницу логина и пароля
    assert driver.current_url == urls.login_url

    # вводим логин
    driver.find_element(By.XPATH, locators.email_input).send_keys(pre_email)

    # вводим пароль
    driver.find_element(By.XPATH, locators.password_input).send_keys(pre_password)

    # нажимаем Войти
    driver.find_element(By.XPATH, locators.locators_button_enter).click()

    # ждем загрузки кнопки Оформить заказ
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.locators_create_order)))

    # после входа поверяем что перекинуло на главную страницу сайта
    assert driver.current_url == urls.main_url

    # закрываем браузер
    driver.quit()
