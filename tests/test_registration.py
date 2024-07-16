from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# сценарий регистрации с генерацией имени, почты, пароля
def test_registation(name_generator, mail_generator, password_generator):
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

    # генерируем пароль
    password = password_generator
    driver.find_element(By.XPATH,
                        "//*[@id='root']/div/main/div/form/fieldset[3]/div/div/input").send_keys(password)
    # сохраняем значение
    value_password = driver.find_element(By.XPATH,
                                         "//*[@id='root']/div/main/div/form/fieldset[3]/div/div/input").get_attribute(
        'value')

    # проверяем что поле пароль заполнено и оно больше или равно 6 символов
    assert password in value_password
    assert value_password >= '6'

    # Жемем кнопку Зарегистрироваться
    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button[text()='Зарегистрироваться']").click()

    # ожидаем форму с логином и паролем, при этом дожидаясь кнопки Войти
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH,
                                          "//*[@id='root']/div/main/div/form/button[text()='Войти']")))

    # убедились что ссылка верная
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    # закрываем брайзер
    driver.quit()
