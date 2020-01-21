from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.get(link)
# browser.implicitly_wait(5)

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
text_element = WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button = browser.find_element_by_id('book')
button.click()

# После брони решаем формулу и отправляем решение

num = browser.find_element_by_id("input_value")
x = num.text

x1 = math.log((abs(12 * math.sin(float(int(x))))), math.e)

input1 = browser.find_element_by_id("answer")
input1.send_keys(str(x1))

button = browser.find_element_by_css_selector("#solve")
button.click()
time.sleep(10)

browser.quit()
