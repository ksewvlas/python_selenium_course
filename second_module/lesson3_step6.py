import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://suninjuly.github.io/redirect_accept.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    button_first = browser.find_element(By.CSS_SELECTOR, 'button.trollface')
    button_first.click()

    first_window = browser.window_handles[0]
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    x = browser.find_element(By.ID, 'input_value').text
    result = calc(x)

    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(result)

    button_second = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button_second.click()

finally:
    time.sleep(3)
    browser.quit()
