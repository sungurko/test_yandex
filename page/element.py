from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):
	'''Базовый класс страницы, который инициализируется в каждом классе объекта страницы.
	из документации https://selenium-python.readthedocs.io/page-objects.html'''

	def __set__(self, obj, value):
		'''Устанавливает текст в указанное значение'''
		driver = obj.driver
		WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_name(self.locator))
		driver.find_element_by_name(self.locator).clear()
		driver.find_element_by_name(self.locator).send_keys(value)


	def __get__(self, obj, owner):
		'''Получает текст указанного объекта'''
		driver = obj.driver
		WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_name(self.locator))
		element = driver.find_element_by_name(self.locator)
		return element.get_attribute("value")

