from selenium.webdriver.remote.webdriver import WebDriver

from page_object.base_page import BasePage


class CreateAccountPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)