from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

browser=webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

button=browser.find_element_by_id("book")
price = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button.click()

submit=browser.find_element_by_id("solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
value_x=browser.find_element_by_id("input_value")
x=value_x.text
y=str(math.log(abs(12*math.sin(int(x)))))
input_robot=browser.find_element_by_id("answer")
input_robot.send_keys(y)
submit.click()
time.sleep(30)
webdriver.quit()
