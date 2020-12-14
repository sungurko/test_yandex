from selenium.webdriver.common.by import By


class MainPageLocators(object):
	INPUT = (By.ID, 'text') # поисковая строка
	SUGGEST=(By.CSS_SELECTOR, 'li[id^="suggest-item-"]') # таблица с подсказками (suggest)
	LINKS = (By.XPATH, "//a[@class='link link_theme_outer path__item i-bem']") # локатор результатов поиска
	TEXT = (By.LINK_TEXT, 'Картинки')
	CLASS_NAME = (By.CLASS_NAME, 'Link')
	CLASS_NAME1=(By.CLASS_NAME, 'serp-item__link')
	CLASS_NAME2=(By.CLASS_NAME, 'input__control')



