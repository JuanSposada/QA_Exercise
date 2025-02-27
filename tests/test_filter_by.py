import pytest
from conftest import driver
from page_object.filter_page import FilterPage


class TestFilterBy:

    @pytest.mark.filter
    def test_filter_by_brand(self, driver):
        filter_page = FilterPage(driver)
        filter_page.open()
        filter_page.filter_by_brand()

    @pytest.mark.filter
    def test_filter_by_size(self, driver):
        filter_page = FilterPage(driver)
        filter_page.open()
        filter_page.filter_by_size()

    @pytest.mark.filter
    def test_filter_by_range(self,driver):
        filter_page = FilterPage(driver)
        filter_page.open()
        filter_page.filter_by_range()





