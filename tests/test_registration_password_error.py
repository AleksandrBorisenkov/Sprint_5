from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# проверили вывод ошибки длины пароля при регистрации
def test_registration_password_error(name_generator, mail_generator, password_generator):
    # настройки браузера в инкогнито, а то кэш портит ввод данных формы
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)

    # начали с формы регистрации
    driver.get('https://stellarburgers.nomoreparties.site/register')

    # ждем загрузки формы
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH,
                                          "//*[@id='root']/div/main/div/form")))

    # убеждаемся что в форме есть 3 инпута для регистрации
    reg_form = driver.find_elements(By.CSS_SELECTOR, ".input__container")
    assert len(reg_form) == 3

    # генерируем имя
    name = name_generator
    driver.find_element(By.XPATH,
                        "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input").send_keys(name)

    value_name = driver.find_element(By.XPATH,
                                     "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input").get_attribute(
        'value')
    # проверяем что поле Имя заполнено
    assert name in value_name

    # генерируем почту
    email = mail_generator
    driver.find_element(By.XPATH,
                        "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input").send_keys(email)
    value_email = driver.find_element(By.XPATH,
                                      "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input").get_attribute(
        'value')

    # проверяем что почта заполнена
    assert email in value_email

    # передаем пароль 5 символов
    password = '12345'
    driver.find_element(By.XPATH,
                        "//*[@id='root']/div/main/div/form/fieldset[3]/div/div/input").send_keys(password)
    # сохраняем значение
    value_password = driver.find_element(By.XPATH,
                                         "//*[@id='root']/div/main/div/form/fieldset[3]/div/div/input").get_attribute(
        'value')

    # проверяем что поле пароль заполнено
    assert password in value_password

    # Жемем кнопку Зарегистрироваться
    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button[text()='Зарегистрироваться']").click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/p")))

    error_password = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/p").text
    assert error_password == 'Некорректный пароль'

    # закрываем брайзер
    driver.quit()
