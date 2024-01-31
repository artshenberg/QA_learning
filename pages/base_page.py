from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from elements.logger import Logger
from elements.wait_conditions import presence_of_element


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.logger = Logger(self.__class__.__name__)

    def open(self, url: str) -> None:
        try:
            self.driver.get(url)
            presence_of_element(self.driver, By.XPATH, '//body')  # Wait for the page to load
        except Exception as e:
            raise e

