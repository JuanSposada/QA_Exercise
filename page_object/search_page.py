from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_object.base_page import BasePage


class SearchPage(BasePage):

    __listing_products_element = (By.CLASS_NAME, 'o-listing__products')
    __brand_cards = (By.CLASS_NAME, "a-card-brand")
    __card_description = (By.CLASS_NAME, "a-card-description")
    __search_input = (By.ID, "mainSearchbar")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)


    def is_listing_products_displayed(self):
        super()._wait_until_element_is_visible(self.__listing_products_element)
        return super()._is_displayed(self.__listing_products_element)



    def is_brand_matching_results(self):
        super()._wait_until_elements_are_visible(self.__brand_cards)
        cards = super()._find_elements(self.__brand_cards)
        cards_text = [card.text for card in cards]
        return super()._get_input_value(self.__search_input).upper() in cards_text


    def is_physical_characteristics_matching_results(self):
        super()._wait_until_elements_are_visible(self.__card_description)
        description = super()._find_elements(self.__card_description)
        description_text = [desc.text.lower() for desc in description]
        characteristics = super()._get_input_value(self.__search_input).lower().split()
        print('ch: ', characteristics, 'desc: ', description_text)
        return [word for word in characteristics if any(word in desc for desc in description_text)]


    def is_model_matching_results(self):
        return self.is_physical_characteristics_matching_results()