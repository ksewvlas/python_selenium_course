import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


link = 'http://suninjuly.github.io/explicit_wait2.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 12).until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, 'h5[id=price]'), '100'))
    button_book = browser.find_element(By.ID, 'book')
    button_book.click()

    x = browser.find_element(By.ID, 'input_value').text
    result = calc(x)
    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(result)
    button_solve = browser.find_element(By.CSS_SELECTOR, 'button[id=solve]')
    button_solve.click()


finally:
    time.sleep(3)
    browser.quit()
