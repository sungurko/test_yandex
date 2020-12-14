import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from page import page
import time


class Yandex(unittest.TestCase):
	'''Картинки на яндексе'''

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path='./chromedriver')
		self.driver.get('https://yandex.ru/')

	def test_image_yandex(self):
		main_page = page.MainPage(self.driver) # загрузка главной страницы yandex.ru
		assert main_page.check_image(), ('Ссылки нет')# Проверить что есть ссылка
		main_page.check_image().click()
		time.sleep(5)
		main_page.tab_switch(1) # переключиться на вторую вкладку
		assert main_page.current_url()[:25] == 'https://yandex.ru/images/', ('url отличается') # проверить url, на который перешли
		time.sleep(5)
		img = main_page.open_top()[0]
		img.click()
		assert img.get_attribute('href') == main_page.current_url(), ('Не открылась') # проверить что открылось при нажатии на 1 категорию
		assert img.get_attribute('text') == main_page.input_text().get_attribute('value'), ('Текст в поиске отличается')
		time.sleep(5)
		img1 = main_page.open_img()[0]
		img1.click()
		time.sleep(5)
		assert img1.get_attribute('href').split('&')[3] == main_page.current_url().split('&')[4], ('Не открылась')
		first_image=main_page.current_url().split('&')[3]
		img1.send_keys(Keys.RIGHT)
		time.sleep(5)
		img1.send_keys(Keys.LEFT)
		time.sleep(5)
		assert main_page.current_url().split('&')[3] == first_image, ('Картинки разные')

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()

