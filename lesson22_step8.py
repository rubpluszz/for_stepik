from selenium import webdriver
import os

browser=webdriver.Chrome()
current_dir = os.path.abspath(os.path.dirname(__file__))  
file_path=os.path.join(current_dir, 'test_load.txt')
link="http://suninjuly.github.io/file_input.html"
browser.get(link)

first_name=browser.find_element_by_name("firstname")
first_name.send_keys("A")

last_name=browser.find_element_by_name("lastname")
last_name.send_keys("B")
email=browser.find_element_by_name("email")
email.send_keys("@")


upload=browser.find_element_by_name("file")
upload.send_keys(file_path)


submit=browser.find_element_by_tag_name("button")
submit.click()
