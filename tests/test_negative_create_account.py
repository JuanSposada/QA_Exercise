import pytest

from page_object.create_account_page import CreateAccountPage


class TestNegativeCrateAccount:
    @pytest.mark.negative
    @pytest.mark.negative_create_account
    @pytest.mark.parametrize(
        "email, password",
        [("supertest12@test.com", "Testing123")])
    def test_negative_create_account_used_email(self, driver, email, password):
        create_account_page = CreateAccountPage(driver)
        create_account_page.open()
        create_account_page.enter_create_account()
        create_account_page.type_password_and_email_for_account(email, password)
        assert create_account_page.is_error_email()

    @pytest.mark.negative
    @pytest.mark.negative_create_account
    @pytest.mark.parametrize(
        "email, password, name, last_name, second_last_name, day, month, year, genre, phone_number",
        [("supertesteado2@test.com", "Testing123", "juan", "moreno", "posada", "2", "Dic", "2000", "hombre",
          "1233332443355676576878899609790770")])
    def test_invalid_phone(self, driver, email, password, name, last_name, second_last_name, day, month, year, genre,
                            phone_number):
        create_account_page = CreateAccountPage(driver)
        create_account_page.open()
        create_account_page.enter_create_account()
        create_account_page.type_password_and_email_for_account(email, password)
        create_account_page.enter_user_data(
            name, last_name, second_last_name, day, month,
            year, genre)
        create_account_page.enter_phone_number(phone_number)
        assert create_account_page.is_error_phone()


