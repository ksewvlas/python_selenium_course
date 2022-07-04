import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/math.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_el = browser.find_element(By.ID, 'input_value')
    x = x_el.text
    result = calc(x)
    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(result)
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()


finally:
    time.sleep(5)
    browser.quit()
