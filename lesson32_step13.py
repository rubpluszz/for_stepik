import unittest #Подключаем фраемворк unittest
from selenium import webdriver # Подключаем елемент вебдрайвер из библиотеки силениум
import time # Подключаем библиотеку управления временем

link_one = "http://suninjuly.github.io/registration1.html" #Ссылка на первый вариант страницы
link_thwo = "http://suninjuly.github.io/registration2.html" #Ссылка на второй вариант страницы

class TestAbs(unittest.TestCase):

	
	def test_thwo(self):
		try: # блок try 
			browser=webdriver.Chrome() # присвоение переменной Браузера
			browser.get(link_thwo)#..новый вариант страницы
			#Поиск соответствующих полей и ввод данных. Поиск всех полей проводитсяп селекторам. 
			input_first_name = browser.find_element_by_css_selector(".first_block>.first_class>.first")
			input_first_name.send_keys("Grzegosz")#Гжегош
			input_last_name = browser.find_element_by_css_selector(".first_block>.second_class>.second")
			input_last_name.send_keys("Brzęczyszczykiewicz")#Бжеженщикевичь
			input_email = browser.find_element_by_css_selector(".first_block>.third_class>.third")
			input_email.send_keys("grzegosz@brzerzyszczykiewicz.pl")
			input_phone = browser.find_element_by_css_selector(".second_block>.first_class>.first")
			input_phone.send_keys("911")
			input_address = browser.find_element_by_css_selector(".second_block>.second_class>.second")
			input_address.send_keys("Chrząszczyżewoszyce")#Хжонщижевошице,
			#Поиск кнопки "Submit" осуществляется по тегу. 
			submit = browser.find_element_by_tag_name("button")
			submit.click()#Отправка данных
		
		finally: #блок уборки.
			browser.quit()#Закрываем браузер
	def test_one(self):
		try: # блок try 
			browser=webdriver.Chrome() # присвоение переменной Браузера
			browser.get(link_one)#..старый вариант страницы
			#Поиск соответствующих полей и ввод данных. Поиск всех полей проводитсяп селекторам. 
			input_first_name = browser.find_element_by_css_selector(".first_block>.first_class>.first")
			input_first_name.send_keys("Grzegosz")#Гжегош
			input_last_name = browser.find_element_by_css_selector(".first_block>.second_class>.second")
			input_last_name.send_keys("Brzęczyszczykiewicz")#Бжеженщикевичь
			input_email = browser.find_element_by_css_selector(".first_block>.third_class>.third")
			input_email.send_keys("grzegosz@brzerzyszczykiewicz.pl")
			input_phone = browser.find_element_by_css_selector(".second_block>.first_class>.first")
			input_phone.send_keys("911")
			input_address = browser.find_element_by_css_selector(".second_block>.second_class>.second")
			input_address.send_keys("Chrząszczyżewoszyce")#Хжонщижевошице,
			#Поиск кнопки "Submit" осуществляется по тегу. 
			submit = browser.find_element_by_tag_name("button")
			submit.click()#Отправка данных
		
		finally: #блок уборки.
			browser.quit()#Закрываем браузер
if __name__ == "__main__":
	unittest.main()
