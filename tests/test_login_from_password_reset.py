from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_from_password_reset():
    # настройки браузера в инкогнито, а то кэш портит ввод данных формы
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)

    # начинаем с формы сброса пароля
    driver.get('https://stellarburgers.nomoreparties.site/reset-password')

    # ждем появление линка "Войти"
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH,
                                          "//*[@id='root']/div/main/div/div/p/a[text()='Войти']")))

    # жмем по линку Войти
    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/div/p/a[text()='Войти']").click()

    #ждем загрузки формы с лоигном и паролем
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/main/div/form")))

    # проверяем что вышли на страницу логина и пароля
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    # вводим логин
    driver.find_element(By.XPATH,
                        "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input").send_keys('AleksandrBorisenkov11666@yandex.ru')

    # вводим пароль
    driver.find_element(By.XPATH,
                        ".//input[@type='password']").send_keys('QWERTY!@#')

    # нажимаем Войти
    driver.find_element(By.XPATH,
                        "//*[@id='root']/div/main/div/form/button[text()='Войти']").click()

    # ждем загрузки кнопки Оформить заказ
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/main/section["
                                                                                "2]/div/button[text()='Оформить заказ']")))

    # после входа поверяем что перекинуло на главную страницу сайта
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    # закрываем браузер
    driver.quit()
