import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get(" http://suninjuly.github.io/cats.html")
browser.implicitly_wait(5)
browser.find_element(By.ID, "button")

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(3)
# закрываем браузер после всех манипуляций
browser.quit()