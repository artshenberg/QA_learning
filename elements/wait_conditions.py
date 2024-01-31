from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


def presence_of_element(driver, by: str, value: str, timeout: int = 10) -> WebElement:
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )


def visibility_of_element(driver, element: WebElement, timeout: int = 10) -> WebElement:
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of(element)
    )


def element_to_be_clickable(driver, element: WebElement, timeout: int = 10) -> WebElement:
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(element)
    )


def wait_for_element_visible(driver, locator, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
    except TimeoutException:
        raise TimeoutException(f"Element {locator} not visible within {timeout} seconds.")


def wait_for_element_clickable(driver, locator, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
    except TimeoutException:
        raise TimeoutException(f"Element {locator} not clickable within {timeout} seconds.")
