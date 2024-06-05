import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_registration1():
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")

    # Заполнение обязательных полей
    browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("First Name")
    browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Last Name")
    browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("Email")

    # Отправка формы
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Проверка успешной регистрации
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text
    browser.quit()

def test_registration2():
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")

    # Заполнение обязательных полей
    browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("First Name")
    browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Last Name")
    browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("Email")

    # Отправка формы
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Проверка успешной регистрации
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text
    browser.quit()




