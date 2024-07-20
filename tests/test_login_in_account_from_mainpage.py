from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators
import urls


# процедура входа в личный кабинет
def test_login_in_account_from_mainpage(driver, pre_email, pre_password):

    # открыли главную страницу
    driver.get(urls.main_url)

    # ждем появление кнопки "Войти в аккаунт"
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

    # дожиаемся появления кнопки Личный кабинет в шапке
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.locators_header_personal_account)))

    # кликаем по иконке личный кабинет
    driver.find_element(By.XPATH, locators.locators_header_personal_account).click()

    # ждем загрузки шапки сайта
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.main_header)))

    # проверяем что зашли в личный кабинет
    assert driver.current_url == urls.profile_url

    # закрываем браузер
    driver.quit()
