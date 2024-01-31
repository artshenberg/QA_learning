# test_framework_example.py
import pytest
from pages.login_page import LoginPage
from elements.browser_factory import BrowserFactory


class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.browser_factory = BrowserFactory()
        self.driver = self.browser_factory.get_driver()
        self.login_page = LoginPage(self.driver)
        yield
        self.browser_factory.close_driver()

    def test_successful_login(self):
        self.login_page.open("http://localhost:7080/login")
        self.login_page.login("tomsmith", "SuperSecretPassword")
        # Add assertions based on your application behavior

    def test_failed_login(self):
        self.login_page.open("http://localhost:7080/login")
        self.login_page.login("invalid_user", "invalid_pass")
        # Add assertions based on your application behavior
