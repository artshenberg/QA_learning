from selenium.common.exceptions import NoSuchElementException
from elements.browser_factory import BrowserFactory
from elements.logger import Logger
from elements.wait_conditions import wait_for_element_visible, wait_for_element_clickable


class BaseElement:
    def __init__(self, locator: tuple, name: str):
        self.locator = locator
        self.name = name
        self.logger = Logger(name)

    def find(self):
        try:
            return BrowserFactory.get_driver().find_element(*self.locator)
        except NoSuchElementException as e:
            self.logger.error(f"Element {self.name} not found: {e}")
            raise e

    def send_keys(self, value):
        element = self.find()
        element.clear()
        element.send_keys(value)

    def click(self):
        element = self.find()
        element.click()

    def wait_for_visible(self, timeout=10):
        wait_for_element_visible(BrowserFactory.get_driver(), self.locator, timeout)

    def wait_for_clickable(self, timeout=10):
        wait_for_element_clickable(BrowserFactory.get_driver(), self.locator, timeout)

    def get_text(self):
        element = self.find()
        return element.text

    def get_attribute(self, attribute_name):
        element = self.find()
        return element.get_attribute(attribute_name)

    def is_displayed(self):
        element = self.find()
        return element.is_displayed()

    def is_enabled(self, driver):
        element = self.find()
        return element.is_enabled()

    def is_selected(self):
        element = self.find()
        return element.is_selected()
