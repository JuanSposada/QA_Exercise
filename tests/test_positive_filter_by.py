import pytest
from conftest import driver
from page_object.filter_page import FilterPage
from page_object.home_page import HomePage


class TestFilterBy:

    @pytest.mark.filter
    @pytest.mark.parametrize("query",["smart tv", "smartphone", "lavadora"])
    def test_filter_by_brand(self, driver, query):
        home_page = HomePage(driver)
        home_page.open()
        search_page = home_page.search(query)
        assert search_page.is_listing_products_displayed(), "Entry Query not displayed"
        filter_page = FilterPage(driver)
        filter_page.filter_by_brand()


    @pytest.mark.filter
    @pytest.mark.parametrize("query", ["smart tv", "smartphone", "lavadora"])
    def test_filter_by_size(self, driver, query):
        home_page = HomePage(driver)
        home_page.open()
        search_page = home_page.search(query)
        assert search_page.is_listing_products_displayed(), "Entry Query not displayed"
        filter_page = FilterPage(driver)
        assert filter_page.filter_by_size(), "Size is not displayed in description"

    @pytest.mark.filter
    @pytest.mark.parametrize("query", ["smart tv", "smartphone", "lavadora"])
    def test_filter_by_range(self,driver, query):
        home_page = HomePage(driver)
        home_page.open()
        search_page = home_page.search(query)
        assert search_page.is_listing_products_displayed(), "Entry Query not displayed"
        filter_page = FilterPage(driver)
        assert filter_page.filter_by_range(), "Size is not displayed in description"

    @pytest.mark.prueba
    def test_filter_prueba(self,driver):
        home_page = HomePage(driver)
        home_page.open()
        search_page = home_page.search("smart TV")
        assert search_page.is_listing_products_displayed(), "Entry Query not displayed"
        filter_page = FilterPage(driver)
        filter_page.filter_by_brand()





