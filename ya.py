from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

binary_yandex_driver_file = r'C:\Users\adene\Downloads\yandexdriver-24.1.0.2570-win64\yandexdriver.exe' # path to YandexDriver

options = webdriver.ChromeOptions()

service = ChromeService(executable_path=binary_yandex_driver_file)
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://yandex.ru')