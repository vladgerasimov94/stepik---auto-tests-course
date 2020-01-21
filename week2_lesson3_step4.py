from  selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector('.btn')
button.click()

confirm = browser.switch_to.alert
confirm.accept()


num = browser.find_element_by_id("input_value")
x = num.text

x1 = math.log((abs(12*math.sin(float(int(x))))), math.e)


input1 = browser.find_element_by_id("answer")
input1.send_keys(str(x1))

button = browser.find_element_by_css_selector(".btn")
button.click()
time.sleep(10)

browser.quit()

