from selenium import webdriver
import time
import math

browser=webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"

browser.get(link)
browser.find_element_by_tag_name("button").click()

new_window = browser.window_handles[1]
first_window = browser.window_handles[0]
link="http://suninjuly.github.io/redirect_page.html"
browser=webdriver.Chrome()

browser.get(link)
value_x=browser.find_element_by_css_selector("div>label>#input_value")
#x=value_x.text
input=browser.find_element_by_id("answer")
input.send_keys(str(math.log(abs(12*math.sin(int(value_x.text))))))

browser.find_element_by_tag_name("button").click()
