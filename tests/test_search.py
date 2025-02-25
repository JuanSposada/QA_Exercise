import time

import pytest
from conftest import driver
from page_object.home_page import HomePage

class TestSearch:

    @pytest.mark.search
    def test_positive_search(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        home_page.search("smart TV")
        assert home_page.is_search_label_displayed(), "Entry Query not displayed"


    @pytest.mark.search
    @pytest.mark.debug ## implementar parametrizacion para cambiar los datos
    def test_positive_search_by_brand(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        home_page.search("Samsung")
        assert home_page.is_search_label_displayed(), "Entry Query not displayed"

    def test_positive_search_by_brand(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        home_page.search("Samsung")
        assert home_page.is_search_label_displayed(), "Entry Query not displayed"








