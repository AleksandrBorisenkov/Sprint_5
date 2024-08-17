from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators
import urls


# сценарий входа со страницы регистрации
# но не регистрируемся, а переходим на форму ввода логина и пароля
def test_login_from_reg_form(driver, pre_email, pre_password):

    # начали с формы регистрации
    driver.get(urls.reg_url)

    # ждем блока Уже зарегистрирован? Войти
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.locator_allready_reg)))

    # жмем на линк Войти
    driver.find_element(By.XPATH, locators.enter_link).click()

    # ждем форму с формой логином и паролем
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.locators_reg_form)))

    # проверили что ссылка тоже верная
    assert driver.current_url == urls.login_url

    # вводим логин
    driver.find_element(By.XPATH, locators.email_input).send_keys(pre_email)

    # вводим пароль
    driver.find_element(By.XPATH, locators.password_input).send_keys(pre_password)

    # жмем войти
    driver.find_element(By.XPATH, locators.locators_button_enter).click()

    # дожидаем когда прогрузится кнопка Оформить заказ
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.locators_create_order)))

    # проверяем что открлся url главной страницы
    assert driver.current_url == urls.main_url

    # закрываем брайзер
    driver.quit()
