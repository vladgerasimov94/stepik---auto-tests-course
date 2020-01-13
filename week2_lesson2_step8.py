from selenium import webdriver
import os 

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)

firstname = browser.find_element_by_name("firstname")
firstname.send_keys("Vladislav")
lastname = browser.find_element_by_name("lastname")
lastname.send_keys("Grgrgrg")
email = browser.find_element_by_name("email")
email.send_keys("sefds@ya.by")

#with open("file.txt", "w") as file:
#    content = file.write("automationbypython")  # create test.txt file

element = browser.find_element_by_id("file")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
element.send_keys(file_path)

button = browser.find_element_by_css_selector(".btn")
button.click()