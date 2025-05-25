from black.linegen import bracket_split_succeeded_or_raise
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time, math, os

"""

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.XPATH, "//span[@id = \"input_value\"]").text
    y = calc(x_element)
    # select = Select(browser.find_element(By.XPATH, "//select[@id]"))
    # select.select_by_value(str(summa))
    button = browser.find_element(By.XPATH, "//button[@type = \"submit\"]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    result = browser.find_element(By.XPATH, "//input")
    result.send_keys(y)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    element1 = browser.find_element(By.XPATH, "//input[@id = \"robotCheckbox\"]")
    element1.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    element2 = browser.find_element(By.XPATH, "//input[@id = \"robotsRule\"]")
    element2.click()
    button.click()
finally:
    time.sleep(10)

    browser.quit()

x = x_element.get_attribute("valuex")
    y = calc(x)

    element1 = browser.find_element(By.XPATH, "//input[@id = \"answer\"]")
    element1.send_keys(y)

    element2 = browser.find_element(By.XPATH, "//input[@id = \"robotCheckbox\"]")
    element2.click()

    element3 = browser.find_element(By.XPATH, "//input[@id = \"robotsRule\"]")
    element3.click()

    button = browser.find_element(By.XPATH, "//button[@type = \"submit\"]")
    button.click()

from selenium import webdriver

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")

    button.click()

finally:
    time.sleep(10)

    browser.quit()


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(r"C:")
    file_path = os.path.join(current_dir, 'clown.txt')

    first_name = browser.find_element(By.XPATH, "//input[@name = \"firstname\"]")
    first_name.send_keys("Ebalo")

    last_name = browser.find_element(By.XPATH, "//input[@name = \"lastname\"]")
    last_name.send_keys("Privet")

    email = browser.find_element(By.XPATH, "//input[@name = \"email\"]")
    email.send_keys("mister@clown.you")

    file_send = browser.find_element(By.XPATH, "//input[@id = \"file\"]")
    file_send.send_keys(file_path)

    button = browser.find_element(By.XPATH, "//button[@type = \"submit\"]")
    button.click()

finally:
    time.sleep(10)

    browser.quit()



try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    button = browser.find_element(By.XPATH, "//button")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.XPATH, "//span[@id = \"input_value\"]").text
    y = calc(x_element)

    answer = browser.find_element(By.XPATH, "//input")
    answer.send_keys(y)

    button2 = browser.find_element(By.XPATH, "//button[@type = \"submit\"]")
    button2.click()

finally:
    time.sleep(10)

    browser.quit()
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver



try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    texterino = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.XPATH, "//h5[@id=\"price\"]"), "$100")
        )
    button = browser.find_element(By.XPATH, "//button[@id=\"book\"]")
    button.click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.XPATH, "//span[@id = \"input_value\"]").text
    y = calc(x_element)

    answer = browser.find_element(By.XPATH, "//input")
    answer.send_keys(y)

    button2 = browser.find_element(By.XPATH, "//button[@type = \"submit\"]")
    button2.click()
finally:
    time.sleep(10)

    browser.quit()