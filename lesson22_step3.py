from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))	
	
link="http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
value_x = browser.find_element_by_css_selector("h2>#num1")
value_y = browser.find_element_by_css_selector("h2>#num2")
x = value_x.text
y = value_y.text
value0=str(str(int(x)+int(y)))
print(value0)
browser.find_element_by_css_selector("div>#dropdown").click()
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(value0)
	

submit=browser.find_element_by_tag_name("button")
submit.click()
time.sleep(30)	
browser.quit()
	
	
	
