import unittest #Подключаем фраемворк unittest
from selenium import webdriver # Подключаем елемент вебдрайвер из библиотеки силениум
import time # Подключаем библиотеку управления временем

link_one = "http://suninjuly.github.io/registration1.html" #Ссылка на первый вариант страницы
link_thwo = "http://suninjuly.github.io/registration2.html" #Ссылка на второй вариант страницы

class TestAbs(unittest.TestCase):
	def test_(self):
		self.assertEqual (abs(-42)==42, "Should be absolute value of a number")
	
	def test_abs2(self):
		self.assertEqual (abs(-42) == -42, "Should be absolute value of a number")
if __name__ == "__main__":
	unittest.main()
