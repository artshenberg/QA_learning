from selenium.webdriver.common.by import By
from elements.base_element import BaseElement


class InputElement(BaseElement):
    def __init__(self, locator: tuple, name: str):
        super().__init__(locator, name)
