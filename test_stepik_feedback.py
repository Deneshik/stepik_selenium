import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

# Список URL-адресов для тестирования
urls = [
    "https://stepik.org/lesson/236895/step/1",
    # "https://stepik.org/lesson/236896/step/1",
    # "https://stepik.org/lesson/236897/step/1",
    # "https://stepik.org/lesson/236898/step/1",
    # "https://stepik.org/lesson/236899/step/1",
    # "https://stepik.org/lesson/236903/step/1",
    # "https://stepik.org/lesson/236904/step/1",
    # "https://stepik.org/lesson/236905/step/1"
]


@pytest.mark.parametrize('url', urls)
def test_feedback(url):
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)

    try:
        # Открыть страницу
        browser.get(url)

        # Авторизация
        login_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.navbar__auth_login"))
        )
        login_button.click()

        # Ввести логин и пароль
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.NAME, "login"))
        ).send_keys("your login")
        browser.find_element(By.NAME, "password").send_keys("your password")
        browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Дождаться, что поп-ап с авторизацией больше нет
        WebDriverWait(browser, 10).until(
            EC.invisibility_of_element((By.CSS_SELECTOR, "div.modal-dialog"))
        )

        # Вычисление правильного ответа
        answer = math.log(int(time.time()))

        # Найти поле ввода и очистить его
        textarea = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea"))
        )
        textarea.clear()

        # Ввод ответа
        textarea.send_keys(str(answer))

        # Отправка ответа
        submit_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
        )
        submit_button.click()

        # Ожидание фидбека
        feedback = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "pre.smart-hints__hint"))
        ).text

        # Проверка фидбека
        assert feedback == "Correct!", f"Expected 'Correct!', but got '{feedback}'"

    finally:
        browser.quit()


if __name__ == "__main__":
    pytest.main()


