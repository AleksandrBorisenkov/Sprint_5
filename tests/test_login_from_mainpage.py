from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_from_mainpage_in_chrome():
    # настройки браузера в инкогнито, а то кэш портит ввод данных формы
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)

    # заходим на сайт
    driver.get('https://stellarburgers.nomoreparties.site/')

    # ждем появление кнопки "Войти в аккаунт" на главной странице
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                      ".//*[contains(text(), 'Войти в "
                                                                      "аккаунт') and starts-with(@class, "
                                                                      "'button_button')]")))

    # жмем кнопку Войти в аккаунт
    driver.find_element(By.XPATH,
                        ".//*[@id='root']/div/main/section[2]/div/button[text()='Войти в аккаунт']").click()

    # проверяем что вышли на страницу логина и пароля
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    # вводим логин
    driver.find_element(By.XPATH,
                        ".//input[@type='text']").send_keys()
    # вводим пароль
    driver.find_element(By.XPATH,
                        ".//input[@type='password']").send_keys('QWERTY!@#')

    # нажимаем Войти
    driver.find_element(By.XPATH, ".//button[contains(text(),'Войти')]").click()

    # дожидаем когда прогрузится кнопка Оформить заказ
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/main/section["
                                                                                "2]/div/button[text()='Оформить заказ']")))

    # проверяем что открлся url главной страницы
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    # закрываем браузер
    driver.quit()
