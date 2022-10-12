from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()
    time.sleep(1)
    alert = browser.switch_to.alert
    alert.accept()   
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    # заполняем поле результатом вычислений
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # Отправляем заполненную форму
    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()