import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_object.base_page import BasePage


class FilterPage(BasePage):

    __first_brand_checkbox = (By.XPATH, "//div[@id='brandFilterWEB']/div[3]/div/div/input") ##Verificar input de check box
    __second_brand_checkbox = (By.XPATH, "//div[@id='brandFilterWEB']/div[4]")
    __third_brand_checkbox = (By.XPATH, "//div[@id='brandFilterWEB']/div[5]")
    __listing_products_element = (By.CLASS_NAME, 'o-listing__products')
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @pytest.mark.filter
    def filter_by_brand(self): #verificar checkbox
        super()._wait_until_element_is_clickable(self.__first_brand_checkbox)
        super()._click(self.__first_brand_checkbox)
        return super()._is_displayed(self.__listing_products_element)
