import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

def test_add_to_cart_button_present(browser):
    # Открыть страницу товара
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Визуальная проверка языка интерфейса
    time.sleep(30)

    # Проверить наличие кнопки добавления в корзину
    add_to_cart_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket"))
    )
    assert add_to_cart_button is not None, "Add to cart button is not present on the page"





