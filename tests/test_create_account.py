import pytest

from conftest import driver
from page_object.create_account_page import CreateAccountPage


class TestCreateAccount:

    @pytest.mark.create_account
    def test_create_account(self, driver):
        create_account_page = CreateAccountPage(driver)
        create_account_page.open()
        create_account_page.enter_create_account()
        create_account_page.type_password_and_email_for_account("jajaj@sisisi.com", "Nekocha420")