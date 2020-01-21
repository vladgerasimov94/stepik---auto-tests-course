from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_xpath('//button')
button.click()

new_window = browser.window_handles[1]
first_window = browser.window_handles[0]

browser.switch_to.window(new_window)


num = browser.find_element_by_id("input_value")
x = num.text

x1 = math.log((abs(12*math.sin(float(int(x))))), math.e)


input1 = browser.find_element_by_id("answer")
input1.send_keys(str(x1))

button = browser.find_element_by_css_selector(".btn")
button.click()
time.sleep(10)

browser.quit()
# time.sleep(5)

# browser.quit()
