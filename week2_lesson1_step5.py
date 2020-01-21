from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
	
x_element = browser.find_element_by_xpath("//span[@id='input_value']")
x = x_element.text


	
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
y = calc(x)

x_input = browser.find_element_by_xpath("//input[@id='answer']")
x_input.send_keys(y)

	
check_box = browser.find_element_by_css_selector("input#robotCheckbox")
check_box.click()
radio = browser.find_element_by_xpath("//label[@for='robotsRule']")
radio.click()
button = browser.find_element_by_css_selector(".btn")
button.click()

    
		

    # закрываем браузер после всех манипуляций
