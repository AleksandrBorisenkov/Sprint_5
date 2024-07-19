from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# сценарий входа со страницы регистрации
# но не регистрируемся, а переходим на форму ввода логина и пароля
def test_login_from_reg_form(driver, reg_url, login_url, main_url, email_input, password_input, pre_email, pre_password,
                             locator_allready_reg, enter_link, locators_reg_form, locators_button_enter, locators_create_order):

    # начали с формы регистрации
    driver.get(reg_url)

    # ждем блока Уже зарегистрирован? Войти
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, locator_allready_reg)))

    # жмем на линк Войти
    driver.find_element(By.XPATH, enter_link).click()

    # ждем форму с формой логином и паролем
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, locators_reg_form)))

    # проверили что ссылка тоже верная
    assert driver.current_url == login_url

    # вводим логин
    driver.find_element(By.XPATH, email_input).send_keys(pre_email)

    # вводим пароль
    driver.find_element(By.XPATH, password_input).send_keys(pre_password)

    # жмем войти
    driver.find_element(By.XPATH, locators_button_enter).click()

    # дожидаем когда прогрузится кнопка Оформить заказ
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators_create_order)))

    # проверяем что открлся url главной страницы
    assert driver.current_url == main_url

    # закрываем брайзер
    driver.quit()
