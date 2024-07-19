from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_from_password_reset(driver, main_url, reset_pas_url, enter_link, locators_reg_form, login_url, email_input,
                                   pre_email, password_input, pre_password, locators_button_enter, locators_create_order):

    # начинаем с формы сброса пароля
    driver.get(reset_pas_url)

    # ждем появление линка "Войти"
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, enter_link)))

    # жмем по линку Войти
    driver.find_element(By.XPATH, enter_link).click()

    #ждем загрузки формы с лоигном и паролем
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators_reg_form)))

    # проверяем что вышли на страницу логина и пароля
    assert driver.current_url == login_url

    # вводим логин
    driver.find_element(By.XPATH, email_input).send_keys(pre_email)

    # вводим пароль
    driver.find_element(By.XPATH, password_input).send_keys(pre_password)

    # нажимаем Войти
    driver.find_element(By.XPATH, locators_button_enter).click()

    # ждем загрузки кнопки Оформить заказ
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators_create_order)))

    # после входа поверяем что перекинуло на главную страницу сайта
    assert driver.current_url == main_url

    # закрываем браузер
    driver.quit()
