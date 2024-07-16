from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_in_account_from_mainpage():
    # настройки браузера в инкогнито, а то кэш портит ввод данных формы
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)

    # процедура входа в личный кабинет и выхода из него
    # открыли главную страницу
    driver.get('https://stellarburgers.nomoreparties.site/')

    # ждем появление кнопки "Войти в аккаунт"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                      ".//*[@id='root']/div/main/section["
                                                                      "2]/div/button[text()='Войти в "
                                                                      "аккаунт']")))
    # жмем кнопку Войти в аккаунт
    driver.find_element(By.XPATH,
                        ".//*[@id='root']/div/main/section[2]/div/button[text()='Войти в аккаунт']").click()

    # проверяем что вышли на страницу логина и пароля
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    # вводим логин
    driver.find_element(By.XPATH,
                        ".//input[@type='text']").send_keys('AleksandrBorisenkov11666@yandex.ru')
    # вводим пароль
    driver.find_element(By.XPATH,
                        ".//input[@type='password']").send_keys('QWERTY!@#')

    # нажимаем Войти
    driver.find_element(By.XPATH, ".//button[contains(text(),'Войти')]").click()

    # дожиаемся появления кнопки Личный кабинет в шапке
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/header/nav/a/p[text("
                                                                                ")='Личный Кабинет']")))

    # кликаем по иконке личный кабинет
    driver.find_element(By.XPATH, "//*[@id='root']/div/header/nav/a/p[text()='Личный Кабинет']").click()

    # ждем загрузки шапки сайта
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/main/div/nav")))

    # проверяем что зашли в личный кабинет
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    # закрываем браузер
    driver.quit()
