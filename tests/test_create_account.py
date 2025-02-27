import pytest

from conftest import driver
from page_object.create_account_page import CreateAccountPage


class TestCreateAccount:

    @pytest.mark.create_account
    def test_create_account(self, driver):
        create_account_page = CreateAccountPage(driver)
        create_account_page.open()
        create_account_page.enter_create_account()
        create_account_page.type_password_and_email_for_account("m.test@test.com", "Nekocha420")
        create_account_page.enter_user_data(
            'Xavier', 'lopez', 'amarillo', '23', 'Dic',
            '2000', 'hombre')
        create_account_page.enter_phone_number('6861254430')
