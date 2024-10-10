from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


# try:
#     browser = webdriver.Chrome()
#     browser.get(" http://suninjuly.github.io/find_xpath_form")
#     # num = browser.find_element(By.PARTIAL_LINK_TEXT, "224592")
#     # num.click()
#
#     input1 = browser.find_element(By.TAG_NAME, 'input')
#     input1.send_keys("putin")
#     input2 = browser.find_element(By.NAME, 'last_name')
#     input2.send_keys("huylo")
#     input3 = browser.find_element(By.CLASS_NAME, 'city')
#     input3.send_keys("moscow")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("in deep")
#
#     button = browser.find_element(By.XPATH, "//button[text()='Submit']")
#     button.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()



# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements(By.TAG_NAME, "input")
#     for element in elements:
#         element.send_keys("Мой ответ")
#
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()




try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
    input1.send_keys("n")
    input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
    input2.send_keys("b")
    input3 = browser.find_element(By.CLASS_NAME, 'third')
    input3.send_keys("a")
    time.sleep(1)
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
