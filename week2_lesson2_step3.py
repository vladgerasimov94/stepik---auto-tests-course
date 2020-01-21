from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
	
num1 = browser.find_element_by_css_selector("#num1")
num_a = num1.text
num2 = browser.find_element_by_css_selector("#num2")
num_b = num2.text

sum1 = int(num_a) + int(num_b)


select = Select(browser.find_element_by_id("dropdown"))
select.select_by_value(str(sum1)) # ищем элемент


button = browser.find_element_by_css_selector(".btn")
button.click()
#browser.execute_script("alert('Robots at work');")

#browser.quit()

    
		

    # закрываем браузер после всех манипуляций
