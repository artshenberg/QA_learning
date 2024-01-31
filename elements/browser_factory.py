from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from elements.logger import Logger

class BrowserFactory:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logger = Logger("BrowserFactory")
            cls._instance.driver = None
        return cls._instance

    @staticmethod
    def get_driver():
        if BrowserFactory._instance.driver is None:
            BrowserFactory._instance.logger.info("Creating a new WebDriver instance.")
            try:
                service = Service(ChromeDriverManager().install())
                driver = webdriver.Chrome(service=service)
                BrowserFactory._instance.driver = driver
            except Exception as e:
                BrowserFactory._instance.logger.error(f"Failed to create WebDriver instance: {e}")
        return BrowserFactory._instance.driver

    def close_driver(self):
        if BrowserFactory._instance.driver is not None:
            BrowserFactory._instance.logger.info("Closing the WebDriver instance.")
            try:
                BrowserFactory._instance.driver.quit()
                BrowserFactory._instance.driver = None
            except Exception as e:
                BrowserFactory._instance.logger.error(f"Failed to close WebDriver instance: {e}")
