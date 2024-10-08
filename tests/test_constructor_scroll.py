from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import locators
import urls


# кликаем на логотип конструктор из аккаунта
def test_construction_scroll(driver):
    # открыли главную страницу
    driver.get(urls.main_url)

    # ждем появления блока бургерами (блок конструктор где собираешь себе бургер)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locators.locators_burger_section)))

    # делаем скрол к соусам
    scroll_sauces = driver.find_element(By.XPATH, locators.locators_souces)
    driver.execute_script("arguments[0].scrollIntoView();", scroll_sauces)

    # делаем скрол к булкам
    scroll_bun = driver.find_element(By.XPATH, locators.locators_bun)
    driver.execute_script("arguments[0].scrollIntoView();", scroll_bun)

    # делаем скрол к ингридиентам
    scroll_ingredients = driver.find_element(By.XPATH, locators.locators_ingredients)
    driver.execute_script("arguments[0].scrollIntoView();", scroll_ingredients)

    # закрываем браузер
    driver.quit()
