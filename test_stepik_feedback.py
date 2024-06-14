import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import math

# Список URL-адресов для тестирования
urls = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]


@pytest.mark.parametrize('url', urls)
def test_feedback(url):
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(10)

    # Открыть страницу
    driver.get(url)

    # Авторизация
    login_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.navbar__auth_login"))
    )
    login_button.click()

    # Ввести логин и пароль
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.NAME, "login"))
    ).send_keys("adeneshik@mail.ru")
    driver.find_element(By.NAME, "password").send_keys("Parabelum33")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Дождаться, что поп-ап с авторизацией больше нет
    WebDriverWait(driver, 5).until(
        EC.invisibility_of_element((By.CSS_SELECTOR, "div.modal-dialog"))
    )

    # Вычисление правильного ответа
    answer = math.log(int(time.time()))


    # Ловим кнопку Решить снова
    try:
        repeat_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".again-btn.white")))
        repeat_button.click()
    except TimeoutException:
        pass

    # Ввод ответа

    textarea = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.textarea")))
    textarea.send_keys(str(answer))

    # Отправка ответа
    submit_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    )
    submit_button.click()

    # Ожидание фидбека
    feedback = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    ).text

    # Проверка фидбека
    print(feedback)

    driver.quit()

