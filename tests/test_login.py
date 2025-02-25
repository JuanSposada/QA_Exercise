import pytest

from page_object.login_page import LoginPage


class TestLogin:

    @pytest.mark.login
    def test_login(self, driver):
        login_page = LoginPage(driver)
        login_page.login()

