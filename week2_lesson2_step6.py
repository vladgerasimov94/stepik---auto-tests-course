from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
	
num = browser.find_element_by_id("input_value")
x = num.text


x1 = math.log((abs(12*math.sin(float(int(x))))), math.e)


input1 = browser.find_element_by_id("answer")
button = browser.find_element_by_css_selector(".btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", input1)


input1.send_keys(str(x1))


check_box = browser.find_element_by_css_selector("input#robotCheckbox")
check_box.click()
radio = browser.find_element_by_xpath("//input[@id='robotsRule']")
radio.click()

button.click()

    
		

    # закрываем браузер после всех манипуляций
