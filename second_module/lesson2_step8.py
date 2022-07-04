import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    fields = browser.find_elements(By.CSS_SELECTOR, 'input:required[type = text]')
    for field in fields:
        field.send_keys('just_value')

    file_name = 'test.txt'
    dir_path = os.path.abspath((os.path.dirname(__file__)))
    file_path = os.path.join(dir_path, file_name)

    file_field = browser.find_element(By.ID, 'file')
    file_field.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, 'button[type = submit].btn')
    button.click()

finally:
    time.sleep(3)
    browser.quit()
