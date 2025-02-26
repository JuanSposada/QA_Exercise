from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_object.base_page import BasePage


class CreateAccountPage(BasePage):

    __url= "https://login.liverpool.com.mx/u/login"
    __create_account_link = (By.LINK_TEXT, 'Crear cuenta')
    __email__field = (By.ID, 'email')
    __password_field = (By.ID, 'password')
    __create_button = (By.XPATH, '//div[@class="c574b8c0d"]/button' )
    __name_field = (By.ID, 'input-user__name')
    __last_name = (By.ID, 'input-user__apaterno')
    __second_last_name = (By.ID, 'input-user__amaterno')
    __date_day_selector_label = (By.ID, 'daySelectorLabel')
    __date_month_selector_label = (By.ID, 'monthSelectorLabel')
    __date_year_selector_label = (By.ID, 'yearSelectorLabel')
    __female_input_radio = (By.ID, 'female')
    __male_input_radio = (By.ID, 'male')
    __create_button_data_form = (By.XPATH, '//button[@class="a-btn a-btn--primary"]')
    __phone_input_field = (By.ID, 'phone')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def enter_create_account(self):
        super()._find(self.__create_account_link).click()

    def type_password_and_email_for_account(self, email: str, password: str):
        super()._type(self.__email__field, email )
        super()._type(self.__password_field, password)
        super()._click(self.__create_button)

    def enter_user_data(self, name: str, lastname: str, secondlastname: str, day: int, month: int, year: int):
        pass





