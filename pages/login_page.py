from pages.base_page import BasePage
from elements.button_element import ButtonElement
from elements.input_element import InputElement
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    # LoginPage elements
    USERNAME_INPUT = InputElement((By.ID, 'username'), 'Username Input')
    PASSWORD_INPUT = InputElement((By.ID, 'password'), 'Password Input')
    LOGIN_BUTTON = ButtonElement((By.XPATH, '//*[contains(text(), "Login")]'), 'Login Button')

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username: str, password: str) -> None:
        try:
            self.USERNAME_INPUT.send_keys(username)
            self.PASSWORD_INPUT.send_keys(password)
            self.LOGIN_BUTTON.click()
            self.logger.info(f"Logged in with username: {username}.")
        except Exception as e:
            self.logger.error(f"Failed to log in with username: {username}. {e}")
            raise e


