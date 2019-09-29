import pytest
from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def aTimeCalc():
	answer = math.log(int(time.time()))
	return answer


#pytest.mark.parametrize)
@pytest.mark.parametrize('getLink', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def testSpaceInvaders(getLink):
	print(f"step=/{getLink}/")
	browser = webdriver.Chrome()
	print("Starting browser")
	browser.get(getLink)
	print("Get to page")
	browser.implicitly_wait(20)
	print("Waitining")
	textArea=browser.find_element_by_class_name("textarea")
	print("Find text area")
	x=aTimeCalc()
	textArea.send_keys(str(x))
	print("Input")
	button=WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "submit-submission")))
	print("Find button")
	button.click()
	print("click button")
	feedback=WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
	if feedback!=("Correct!"):
		print(f"It's not correct vallue. Vallue=/{feedback}/")
	if feedback==("Correct!"):
		print("correct vallue")
	browser.quit()	
	
