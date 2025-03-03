import pytest

from conftest import driver
from page_object.create_account_page import CreateAccountPage


class TestCreateAccount:

    @pytest.mark.create_account
    @pytest.mark.parametrize(
        "email, password, name, last_name, second_last_name, day, month, year, genre, phone_number",
        [("supertest12@test.com", "Testing123", "juan", "moreno", "posada", "2", "Dic", "2000", "hombre",
         "6861234567")])
    def test_create_account(self, driver, email, password, name, last_name, second_last_name, day, month, year, genre,
                            phone_number):
        create_account_page = CreateAccountPage(driver)
        create_account_page.open()
        create_account_page.enter_create_account()
        create_account_page.type_password_and_email_for_account(email, password)
        create_account_page.enter_user_data(
            name, last_name, second_last_name, day, month,
            year, genre)
        create_account_page.enter_phone_number(phone_number)
