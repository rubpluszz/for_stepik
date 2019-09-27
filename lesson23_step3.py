from selenium import webdriver
import math
import time
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"

browser.get(link)

button_one = browser.find_element_by_css_selector("div>.btn")
button_one.click()

confirm = browser.switch_to.alert
confirm.accept()

value_x=browser.find_element_by_id("input_value")
x=value_x.text
y=str(math.log(abs(12*math.sin(int(x)))))

input_robot=browser.find_element_by_css_selector("div>#answer")
input_robot.send_keys(y)

submit = browser.find_element_by_css_selector("div>.btn")
submit.click()


time.sleep(30)

confirm = browser.switch_to.alert #Нажать ок вмодальном окне
confirm.accept()

browser.quit()
