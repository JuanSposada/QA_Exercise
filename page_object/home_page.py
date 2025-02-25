from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_object.base_page import BasePage
from page_object.search_page import SearchPage


class HomePage(BasePage):

    __url = 'https://www.liverpool.com.mx/tienda/home'
    __search_input = (By.ID, "mainSearchbar")
    __search_button = (By.XPATH, '//*[@id="sayt"]/div[1]/div/div/button[2]')
    __search_entry_label = (By.XPATH, '//*[@id="__next"]/main/div[2]/div[1]/div/div[3]/div[1]/div/div/div/ul/li[2]/span/strong')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def search(self, text):
        super()._type(self.__search_input, text)
        super()._click(self.__search_button)
        return SearchPage(self._driver)












    