from selenium import webdriver
import math
import time

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))	
	
link="http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
value_x = browser.find_element_by_css_selector("h2>#treasure")
image_kod=value_x.get_attribute("valuex")

x = image_kod
y =calc(x)
	
input_robot = browser.find_element_by_tag_name("input")
input_robot.send_keys(y)

check_box = browser.find_element_by_css_selector("div>#robotCheckbox")
check_box.click()

raduo_button=browser.find_element_by_css_selector("div>#robotsRule")
raduo_button.click()

submit=browser.find_element_by_tag_name("button")
submit.click()
time.sleep(30)	
browser.quit()
	
	
	
