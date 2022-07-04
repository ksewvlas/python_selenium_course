import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    robot_radio = browser.find_element(By.ID, "robotsRule")
    robot_checked = robot_radio.get_attribute("checked")
    print("value of robot radio: ", robot_checked)
    assert robot_checked is None, "Robot radio is selected by default"

    time.sleep(10)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-default')
    button_disable = button.get_attribute('disabled')
    print('value of button: ', button_disable)
    assert button_disable == 'true', 'Button is active'

finally:
    time.sleep(3)
    browser.quit()
