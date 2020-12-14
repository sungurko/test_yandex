import unittest
from selenium import webdriver
from page import page
import time


class Yandex(unittest.TestCase):
	'''Поиск в яндексе'''
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path='./chromedriver')
		self.driver.get('https://yandex.ru/')

	def test_search_yandex(self):
		main_page = page.MainPage(self.driver) # загрузка главной страницы yandex.ru
		assert main_page.check_input_search(), ('Нет поля поиска')
		main_page.search_text_element = "Тензор"
		time.sleep(5)
		assert main_page.check_suggest(), ('Нет таблицы подсказок')
		main_page.enter()
		time.sleep(5)
		result_page=main_page.top_5_result()
		assert 'tensor.ru' in result_page, ('tensor.ru не найден')

	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()

