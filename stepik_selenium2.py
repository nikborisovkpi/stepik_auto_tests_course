from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    # button = browser.find_element(By.TAG_NAME, "button")
    # button.click()
    # alert = browser.switch_to.alert
    # alert.accept()
    # new_window = browser.window_handles[1]
    # browser.switch_to.window(new_window)

    input = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    button = browser.find_element(By.XPATH, "//button[text()='Book']")
    button.click()

    x_element = browser.find_element(By.ID, 'input_value')
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_element)
    x = calc(x_element.text)
    # x = x_element.get_attribute("valuex")
    # y = calc(x)
    # x = browser.find_element(By.ID, 'num1')
    # y = browser.find_element(By.ID, 'num2')
    # answer = str(int(x.text) + int(y.text))

    # select = Select(browser.find_element(By.TAG_NAME, "select"))
    # select.select_by_visible_text(answer)
    # browser.execute_script("window.scrollBy(0, 100);")

    input1 = browser.find_element(By.NAME, 'text')
    input1.send_keys(x)
    # input2 = browser.find_element(By.NAME, 'lastname')
    # input2.send_keys('y')
    # input3 = browser.find_element(By.NAME, 'email')
    # input3.send_keys('z')

    # option1 = browser.find_element(By.ID, "robotCheckbox")
    # option1.click()
    # option2 = browser.find_element(By.ID, "robotsRule")
    # option2.click()

    # element = browser.find_element(By.ID, 'file')
    # current_dir = os.path.dirname(__file__)
    # file_path = os.path.join(current_dir, 'Text Document.txt')
    # element.send_keys(file_path)

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    time.sleep(5)
    browser.quit()