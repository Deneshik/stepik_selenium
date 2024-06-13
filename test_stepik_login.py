import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_stepik_login():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)

    try:
        # Открыть страницу
        browser.get("https://stepik.org/lesson/236895/step/1")

        # Нажать на кнопку авторизации
        login_button = browser.find_element(By.CSS_SELECTOR, "a.navbar__auth_login")
        login_button.click()

        # Ввести логин и пароль
        browser.find_element(By.NAME, "login").send_keys("your_login")
        browser.find_element(By.NAME, "password").send_keys("your_password")
        browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Дождаться, что поп-ап с авторизацией больше нет
        WebDriverWait(browser, 10).until(
            EC.invisibility_of_element((By.CSS_SELECTOR, "div.modal-dialog"))
        )

        # Проверка, что поп-ап исчез
        assert not browser.find_elements(By.CSS_SELECTOR, "div.modal-dialog"), "Login pop-up is still visible"

    finally:
        browser.quit()