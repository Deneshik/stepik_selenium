import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_registration1(self):
        self.browser.get("http://suninjuly.github.io/registration1.html")

        # Заполнение обязательных полей
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("First Name")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Last Name")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("Email")

        # Отправка формы
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Проверка успешной регистрации
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self):
        self.browser.get("http://suninjuly.github.io/registration2.html")

        # Заполнение обязательных полей
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("First Name")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Last Name")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("Email")

        # Отправка формы
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Проверка успешной регистрации
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()


