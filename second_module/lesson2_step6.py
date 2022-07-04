import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/execute_script.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, 'input_value').text
    result = calc(x)

    input_field = browser.find_element(By.ID, 'answer')
    input_field.send_keys(result)

    robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()

    browser.execute_script('return arguments[0].scrollIntoView(true);', robot_checkbox)

    robot_radio = browser.find_element(By.ID, 'robotsRule')
    robot_radio.click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # button.click()
    # button = browser.find_element(By.TAG_NAME, "button")
    # button.click()
    # browser.execute_script('alert("Robots at work!");')
    # browser.execute_script('document.title="Script executing";')
    # browser.execute_script('document.title="Script executing";alert("Robots at work!");')

finally:
    time.sleep(3)
    browser.quit()
