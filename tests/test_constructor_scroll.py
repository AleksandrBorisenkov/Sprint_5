from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_construction_scroll():
    # настройки браузера в инкогнито, а то кэш портит ввод данных формы
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)

    # кликаем на логотип конструктор из аккаунта

    # открыли главную страницу
    driver.get('https://stellarburgers.nomoreparties.site/')

    # ждем появления блока бургерами (блок конструктор где собираешь себе бургер)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/main/section[1]")))

    # делаем скрол к соусам
    scroll_sauces = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/ul[2]")
    driver.execute_script("arguments[0].scrollIntoView();", scroll_sauces)

    # делаем скрол к булкам
    scroll_bun = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/ul[1]")
    driver.execute_script("arguments[0].scrollIntoView();", scroll_bun)

    # делаем скрол к ингридиентам
    scroll_ingredients = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/ul[3]")
    driver.execute_script("arguments[0].scrollIntoView();", scroll_ingredients)

    # закрываем браузер
    driver.quit()
