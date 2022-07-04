import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

link = 'http://suninjuly.github.io/selects2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num_1 = browser.find_element(By.ID, 'num1').text
    print(f'num1: {num_1}')
    num_2 = browser.find_element(By.ID, 'num2').text
    print(f'num2: {num_2}')
    result = int(num_1) + int(num_2)
    print(f'result: {result}')

    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(f'{result}')

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-default')
    button.click()

finally:
    time.sleep(3)
    browser.quit()
