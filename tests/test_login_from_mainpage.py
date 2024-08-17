from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import locators
import urls


def test_login_from_mainpage_in_chrome(driver, pre_email, pre_password):
    # заходим на сайт
    driver.get(urls.main_url)

    # ждем появление кнопки "Войти в аккаунт" на главной странице
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.locators_button_enter_account)))

    # жмем кнопку Войти в аккаунт
    driver.find_element(By.XPATH, locators.locators_button_enter_account).click()

    # проверяем что вышли на страницу логина и пароля
    assert driver.current_url == urls.login_url

    # вводим логин
    driver.find_element(By.XPATH, locators.email_input).send_keys(pre_email)
    # вводим пароль
    driver.find_element(By.XPATH, locators.password_input).send_keys(pre_password)

    # нажимаем Войти
    driver.find_element(By.XPATH, locators.locators_button_enter).click()

    # дожидаем когда прогрузится кнопка Оформить заказ
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.locators_create_order)))

    # проверяем что открлся url главной страницы
    assert driver.current_url == urls.main_url

    # закрываем браузер
    driver.quit()
