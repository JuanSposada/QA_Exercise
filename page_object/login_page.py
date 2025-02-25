from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_object.base_page import BasePage


class LoginPage(BasePage):

    __url = 'https://login.liverpool.com.mx/u/login?state=hKFo2SBWSk90czBsM25DU2ZZU0ZlRGlIMUU4Z2l5ak5haThDRKFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIHJCNWhpdU81aEVCb1d0Sno5UVp0QWpYSTZ0bEhjTUwwo2NpZNkgVXBQSElJaGNGckRuWVRuUW5pWHFBNjFQN1I4ZERtZGY'
    __username_field = (By.ID, 'username')
    __password_field = (By.ID, 'password')
    __login_button = (By.NAME, "action")
    __verification_code_message = (By.TAG_NAME, 'h1')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def login(self, username, password):
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        super()._click(self.__login_button)

    def is_verification_message_displayed(self):
        super()._wait_until_element_is_visible(self.__verification_code_message)
        return super()._is_displayed(self.__verification_code_message)

