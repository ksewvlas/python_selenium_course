from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/registration2.html'


def fill_required_fields():
    first_name = browser.find_element(By.CSS_SELECTOR, 'input.first:required')
    first_name.send_keys('just_value')
    second_name = browser.find_element(By.CSS_SELECTOR, 'input.second:required')
    second_name.send_keys('just_value')
    email = browser.find_element(By.CSS_SELECTOR, 'input.third:required')
    email.send_keys('just_value')


try:
    browser = webdriver.Chrome()
    browser.get(link)

    fill_required_fields()

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
    welcome_text = welcome_text_elt.text

    assert 'Congratulations! You have successfully registered!' == welcome_text

finally:
    time.sleep(5)
    browser.quit()
