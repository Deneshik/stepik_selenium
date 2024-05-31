# import os
#
# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
# element.send_keys(file_path)


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнить текстовые поля: имя, фамилия, email
    first_name = browser.find_element(By.NAME, 'firstname').send_keys("Andrey")
    last_name = browser.find_element(By.NAME, 'lastname').send_keys("Deneshik")
    email = browser.find_element(By.NAME, 'email').send_keys("adeneshik@mail.ru")

    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    file_input = browser.find_element(By.ID, "file")
    # Создаем временный файл
    with open("file.txt", "w") as file:
        file.write("This is a test file.")
    file_path = os.path.abspath("file.txt")
    file_input.send_keys(file_path)

    # Нажимаем на кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    # Удаляем временный файл
    os.remove("file.txt")

# не забываем оставить пустую строку в конце файла
