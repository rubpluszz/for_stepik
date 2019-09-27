from selenium import webdriver
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

value_x = browser.find_element_by_css_selector("label>#input_value")
x=value_x.text
y = calc(x)

input_robot = browser.find_element_by_css_selector("div>#answer")
input_robot.send_keys(y)


button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

check_box = browser.find_element_by_css_selector("div>#robotCheckbox")
check_box.click()

radio_button = browser.find_element_by_css_selector("div>#robotsRule")
radio_button.click()

button.click()
assert True
