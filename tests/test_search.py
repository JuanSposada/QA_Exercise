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


    @pytest.mark.search     ## implementar parametrizacion para cambiar los datos
    def test_positive_search_by_brand(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        home_page.search("Sony")
        assert home_page.is_brand_matching_results(), "Products dont match"

    @pytest.mark.search
    def test_positive_search_by_characteristics(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        home_page.search("bolsa rojo mujer")
        assert home_page.is_physical_characteristics_matching_results(), "Characteristics dont match description"

    @pytest.mark.search  ## implementar parametrizacion para cambiar los datos
    @pytest.mark.debug
    def test_positive_search_by_model(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        home_page.search("qn65q65dafxzx")
        assert home_page.is_model_matching_results(), "Products dont match"









