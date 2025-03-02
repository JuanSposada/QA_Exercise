import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_object.base_page import BasePage


class FilterPage(BasePage):

    ##Verificar input de check box
    __second_brand_checkbox = (By.XPATH, "//div[@id='brandFilterWEB']/div[2]/div/div")
    __second_brand_label = (By.XPATH, "//div[@id='brandFilterWEB']/div[2]/div/label" )
    __third_brand_checkbox = (By.XPATH, "//div[@id='brandFilterWEB']/div[5]")
    __listing_products_element = (By.CLASS_NAME, 'o-listing__products')
    __url= "https://www.liverpool.com.mx/tienda?s=smart+tv"
    __first_brand_checkbox = (By.XPATH, "//div[@id='brandFilterWEB']/div[2]/div/div")
    __first_size_checkbox = (By.XPATH, "//div[@id='TamaocountViewMore0']/div/div")
    __first_size_label = (By.XPATH, "//div[@id='TamaocountViewMore0']/div/label")
    __first_range_radio = (By.XPATH, "//div[@class='fiterl-prices']/div[1]/div")
    __first_range_label = (By.XPATH, "//div[@class='fiterl-prices']/div[1]/label")
    __brand_cards = (By.CLASS_NAME, "a-card-brand")
    __card_description = (By.CLASS_NAME, "a-card-description")
    __cards_price = (By.CLASS_NAME, "a-card-discount")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def filter_by_brand(self):
        super()._click(self.__first_brand_checkbox)
        super()._wait_until_elements_are_visible(self.__brand_cards)
        cards = super()._find_elements(self.__brand_cards)
        cards_text = [card.text for card in cards]
        return super()._get_text(self.__second_brand_label).upper().split(" ")[0] in cards_text

    def filter_by_size(self):
        super()._click(self.__first_size_checkbox)
        super()._wait_until_elements_are_visible(self.__card_description)
        description = super()._find_elements(self.__card_description)
        description_text = [desc.text.lower() for desc in description]
        label_text = super()._get_text(self.__first_size_label).lower().split()[0]
        return  any(label_text in desc for desc in description_text)

    def filter_by_range(self):
        label_price_text_to_int = int(super()._get_text(self.__first_range_label).split("$")[1].split(".")[0])
        print(label_price_text_to_int)
        super()._click(self.__first_range_radio)
        super()._wait_until_elements_are_visible(self.__cards_price)
        prices = super()._find_elements(self.__cards_price)
        prices_text_to_int = [int(price.text.replace("$", "").replace(",", "")[:-2]) for price in prices]
        print(prices_text_to_int, label_price_text_to_int)
        return any(price < label_price_text_to_int for price in prices_text_to_int)

    def filter_test(self):
        super()._click(self.__second_brand_checkbox)
        super()._wait_until_elements_are_visible(self.__brand_cards)
        cards = super()._find_elements(self.__brand_cards)
        cards_text = [card.text for card in cards]
        return super()._get_text(self.__second_brand_label).upper().split(" ")[0] in cards_text




