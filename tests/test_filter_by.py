import time

import pytest
from conftest import driver
from page_object.filter_page import FilterPage
from page_object.home_page import HomePage


class TestFilterBy:

    @pytest.mark.filter
    @pytest.mark.debug
    def test_filter_by_brand(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        home_page.search("smart tv")
        filter_page = FilterPage(driver)
        filter_page.filter_by_brand()
        time.sleep(10)











