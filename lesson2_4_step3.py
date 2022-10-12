import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")
time.sleep(3) #убрать для успешной демонстрации ошибки из урока 3, оставить для 4
button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(3)
# закрываем браузер после всех манипуляций
browser.quit()