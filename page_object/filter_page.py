import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_object.base_page import BasePage


class FilterPage(BasePage):

    ##Verificar input de check box
    __second_brand_checkbox = (By.XPATH, "//div[@id='brandFilterWEB']/div[2]/div/div")
    __third_brand_checkbox = (By.XPATH, "//div[@id='brandFilterWEB']/div[5]")
    __listing_products_element = (By.CLASS_NAME, 'o-listing__products')
    __url= "https://www.liverpool.com.mx/tienda?s=smart+tv"
    __first_brand_checkbox = (By.XPATH, "//div[@id='brandFilterWEB']/div[3]/div/div/input")
    __first_size_checkbox = (By.XPATH, "//div[@id='TamaocountViewMore0']/div/div/input")
    __first_range_radio = (By.XPATH, "//div[@class='fiterl-prices']/div[1]/div/input")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def filter_by_brand(self):
        super()._find(self.__first_brand_checkbox).click()

    def filter_by_size(self):
        super()._find(self.__first_size_checkbox).click()

    def filter_by_range(self):
        super()._find(self.__first_range_radio).click()

    def filter_test(self):
        super()._click(self.__second_brand_checkbox)



