from re import search

import pytest

from conftest import driver
from page_object.filter_page import FilterPage
from page_object.home_page import HomePage


class TestSearch:

    @pytest.mark.search
    @pytest.mark.parametrize("article", [("Smart tv"),("laptop"),("camiseta"), ('perfume')])
    def test_positive_search(self, driver, article):
        home_page = HomePage(driver)
        home_page.open()
        search_page = home_page.search(article)
        assert search_page.is_listing_products_displayed(), "Entry Query not displayed"


    @pytest.mark.search
    @pytest.mark.parametrize("brand", ["sony", "lee", "fabellino"])
    def test_positive_search_by_brand(self, driver, brand):
        home_page = HomePage(driver)
        home_page.open()
        search_page = home_page.search(brand)
        assert search_page.is_brand_matching_results(), "Products dont match"

    @pytest.mark.search
    @pytest.mark.parametrize("physical_characteristic",["bolsa roja mujer", "lentes oscuros", "television chica"])
    @pytest.mark.debug
    def test_positive_search_by_characteristics(self, driver,physical_characteristic):
        home_page = HomePage(driver)
        home_page.open()
        search_page = home_page.search(physical_characteristic)
        assert search_page.is_physical_characteristics_matching_results(), "Characteristics dont match description"

    @pytest.mark.search  ## implementar parametrizacion para cambiar los datos
    def test_positive_search_by_model(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        search_page = home_page.search("qn65q65dafxzx")
        assert search_page.is_model_matching_results(), "Products dont match"

    @pytest.mark.searchTest
    def test_filter_prueba(self,driver):
        home_page = HomePage(driver)
        home_page.open()
        search_page = home_page.search("smart TV")
        assert search_page.is_listing_products_displayed(), "Entry Query not displayed"
        filterpage = FilterPage(driver)
        filterpage.filter_test()





