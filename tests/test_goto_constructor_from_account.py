from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import locators
import urls


# кликаем на логотип конструктор из аккаунта
def test_goto_constructor_from_account(driver, pre_email, pre_password):
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

    # ждем загрузки Rнопки сохранить
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.locators_button_save)))

    # проверяем что зашли в личный кабинет
    assert driver.current_url == urls.profile_url

    # находим элемент иконку Конструктор и климаем по ней
    driver.find_element(By.XPATH, locators.locators_constructor_icon).click()

    # ждем появления блока бургерами (блок конструктор где собираешь себе бургер)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locators.locators_burger_section)))

    # сверяем что это на главной странице
    assert driver.current_url == urls.main_url

    # закрываем браузер
    driver.quit()
