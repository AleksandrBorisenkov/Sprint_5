from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_from_reg_form():
    # настройки браузера в инкогнито, а то кэш портит ввод данных формы
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)

    # сценарий входа со страницы регистрации
    # но не регистрируемся, а переходим на форму ввода логина и пароля

    # начали с формы регистрации
    driver.get('https://stellarburgers.nomoreparties.site/register')

    # ждем блока Уже зарегистрирован? Войти
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH,
                                          "//*[@id='root']/div/main/div/div/p")))

    # жмем на линк Войти
    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/div/p/a[text()='Войти']").click()

    # ждем форму с формой логином и паролем
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH,
                                          "//*[@id='root']/div/main/div/form")))

    # проверили что ссылка тоже верная
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    # вводим логин
    driver.find_element(By.XPATH,
                        "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input").send_keys('AleksandrBorisenkov11666@yandex.ru')

    # вводим пароль
    driver.find_element(By.XPATH,
                        ".//input[@type='password']").send_keys('QWERTY!@#')

    # жмем войти
    driver.find_element(By.XPATH,
                        "//*[@id='root']/div/main/div/form/button[text()='Войти']").click()

    # дожидаем когда прогрузится кнопка Оформить заказ
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/main/section["
                                                                                "2]/div/button[text()='Оформить заказ']")))

    # проверяем что открлся url главной страницы
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    # закрываем брайзер
    driver.quit()
