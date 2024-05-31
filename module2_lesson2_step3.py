from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


link = "https://suninjuly.github.io/selects2.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем значения двух чисел
    num1_element = browser.find_element(By.ID, "num1")
    num2_element = browser.find_element(By.ID, "num2")
    num1 = int(num1_element.text)
    num2 = int(num2_element.text)

    # Считаем их сумму
    sum_value = str(num1 + num2)

    # Выбираем в выпадающем списке значение, равное рассчитанной сумме
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(sum_value)

    # Нажимаем на кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

