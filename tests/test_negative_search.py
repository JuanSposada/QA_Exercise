import time

import pytest

from page_object.home_page import HomePage


class TestNegativeSearch:

    @pytest.mark.negative
    @pytest.mark.negative_search
    @pytest.mark.parametrize("article", ["Sm@rt_tv", "", "c4mis3t@", 'd3r{um3'])
    def test_negative_search(self, driver, article):
        home_page = HomePage(driver)
        home_page.open()
        search_page = home_page.search(article)
        assert search_page.is_null_query_displayed(), "null product not displayed"

    @pytest.mark.negative
    @pytest.mark.negative_search
    @pytest.mark.parametrize("brand", ["$0ny", "c0nbers3", "f@bellyn0"])
    def test_negative_search_by_brand(self, driver, brand):
        home_page = HomePage(driver)
        home_page.open()
        search_page = home_page.search(brand)
        assert search_page.is_null_query_displayed(), "Products are shown"

    @pytest.mark.negative
    @pytest.mark.negative_search
    @pytest.mark.parametrize("model", ["qñ65o65d@fxzx", "“@1f0n31", "LMAo22G"])
    @pytest.mark.debug
    def test_negative_search_model(self, driver,model):
        home_page = HomePage(driver)
        home_page.open()
        search_page = home_page.search(model)
        assert search_page.is_null_query_displayed(), "Products are matching results"
