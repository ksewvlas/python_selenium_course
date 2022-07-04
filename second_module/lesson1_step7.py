import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/get_attribute.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    image = browser.find_element(By.ID, 'treasure')
    secret_x = image.get_attribute('valuex')
    print(secret_x)
    result = calc(secret_x)
    result_field = browser.find_element(By.ID, 'answer')
    result_field.send_keys(result)
    robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()
    robot_radio = browser.find_element(By.ID, 'robotsRule')
    robot_radio.click()
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-default')
    button.click()

finally:
    time.sleep(3)
    browser.quit()
