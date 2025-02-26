from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, \
    visibility_of_all_elements_located, element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple):
        return self._driver.find_element(*locator)
    def _find_elements(self, locator: tuple):
        return self._driver.find_elements(*locator)

    def _type(self, locator: tuple, text: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _wait_until_element_is_visible(self, locator, time: int=10):
        wait = WebDriverWait(self._driver, time)
        wait.until(visibility_of_element_located(locator))

    def _wait_until_elements_are_visible(self, locator, time: int=10):
        wait = WebDriverWait(self._driver, time)
        wait.until(visibility_of_all_elements_located(locator))

    def _wait_until_element_is_clickable(self, locator, time: int=10):
        wait = WebDriverWait(self._driver, time)
        wait.until(element_to_be_clickable(locator))

    def _click(self, locator: tuple, time: int=10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    def _is_displayed(self, locator: tuple):
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _open_url(self, url: str):
        self._driver.get(url)

    def _get_text(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text

    def _clear_input(self, locator: tuple, time: int =10):
        self._wait_until_element_is_clickable(locator, time)
        return self._find(locator).clear()

    def _get_input_value(self, locator: tuple, time: int=10):
        self._wait_until_element_is_clickable(locator)
        return self._find(locator).get_attribute("value")






