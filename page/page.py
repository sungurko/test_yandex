from page.element import BasePageElement
from page.locators import MainPageLocators
from selenium.webdriver.common.keys import Keys


class SearchTextElement(BasePageElement):
	locator = 'text'

class BasePage(object):
    '''Инициализация базовой страницы'''

    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
	'''Действия на странице'''
	search_text_element = SearchTextElement()

	def check_input_search(self):
		element = self.driver.find_element(*MainPageLocators.INPUT)
		return element

	def check_image(self):
		element = self.driver.find_element(*MainPageLocators.TEXT)
		return element

	def check_suggest(self):
		'''таблица с подсказками'''
		suggest=self.driver.find_element(*MainPageLocators.SUGGEST)
		return suggest

	def enter(self):
		'''Enter'''
		element = self.driver.find_element(*MainPageLocators.INPUT)
		element.send_keys(Keys.ENTER)

	def top_5_result(self):
		links=self.driver.find_elements(*MainPageLocators.LINKS)
		top_link=[i.get_attribute('href')[8:17] for i in links][0:5]
		return top_link

	def current_url(self):
		url = self.driver.current_url
		return url

	def tab_switch(self, value):
		tabs = self.driver.window_handles
		self.driver.switch_to.window(tabs[value])
		return tabs

	def open_top(self):
		img = self.driver.find_elements(*MainPageLocators.CLASS_NAME)
		return img

	def open_img(self):
		img1 = self.driver.find_elements(*MainPageLocators.CLASS_NAME1)
		return img1

	def input_text(self):
		input_text = self.driver.find_element(*MainPageLocators.CLASS_NAME2)
		return input_text

