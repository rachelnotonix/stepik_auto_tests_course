from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v136.page import bring_to_front
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time, math, os


class TestRegistration(unittest.TestCase):

    def test_registration_all_required(self):

        try:
            browser = webdriver.Chrome()
            self.link = "http://suninjuly.github.io/registration2.html"
            browser.get(self.link)

            self.first_name = browser.find_element(By.XPATH, "//div[label[contains(text(), 'First name*')]]//input")
            self.first_name.send_keys("zalupa")

            self.last_name = browser.find_element(By.XPATH, "//div[label[contains(text(), 'Last name*')]]//input")
            self.last_name.send_keys("zalupovich")

            self.email = browser.find_element(By.XPATH, "//div[label[contains(text(), 'Email*')]]//input")
            self.email.send_keys("zalupa@com")

            self.button_submit = browser.find_element(By.XPATH, "//button[@type='submit']")
            self.button_submit.click()

            self.checking = browser.find_element(By.XPATH, "//h1").text
            self.assertEqual(self.checking, "Congratulations! You have successfully registered!", "Should be the congratulations message.")

        finally:
            time.sleep(10)
            browser.quit()

    # def test_registration_all_fields(self):
    #
    #     try:
    #         browser = webdriver.Chrome()
    #         self.link = "http://suninjuly.github.io/registration1.html"
    #         browser.get(self.link)
    #
    #         self.first_name = browser.find_element(By.XPATH, "//div[label[contains(text(), 'First name*')]]//input")
    #         self.first_name.send_keys("zalupa")
    #
    #         self.last_name = browser.find_element(By.XPATH, "//div[label[contains(text(), 'Last name*')]]//input")
    #         self.last_name.send_keys("zalupovich")
    #
    #         self.email = browser.find_element(By.XPATH, "//div[label[contains(text(), 'Email*')]]//input")
    #         self.email.send_keys("zalupa@com")
    #
    #         self.phone = browser.find_element(By.XPATH, "//div[label[contains(text(), 'Phone')]]//input")
    #         self.phone.send_keys("12345")
    #
    #         self.address = browser.find_element(By.XPATH, "//div[label[contains(text(), 'Address')]]//input")
    #         self.address.send_keys("zalupinsk")
    #
    #         self.button_submit = browser.find_element(By.XPATH, "//button[@type='submit']")
    #         self.button_submit.click()
    #
    #     finally:
    #
    #         time.sleep(10)
    #         browser.quit()
    #
    # def test_registration_miss_one_required(self):
    #
    #     try:
    #         browser = webdriver.Chrome()
    #         self.link = "http://suninjuly.github.io/registration1.html"
    #         browser.get(self.link)
    #
    #         self.first_name = browser.find_element(By.XPATH, "//div[label[contains(text(), 'First name*')]]//input")
    #         self.first_name.send_keys("zalupa")
    #
    #         self.email = browser.find_element(By.XPATH, "//div[label[contains(text(), 'Email*')]]//input")
    #         self.email.send_keys("zalupa@com")
    #
    #         self.button_submit = browser.find_element(By.XPATH, "//button[@type='submit']")
    #         self.button_submit.click()
    #
    #     finally:
    #         time.sleep(10)
    #         browser.quit()

if __name__ == "__main__":
    unittest.main()