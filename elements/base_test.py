import pytest
from elements.browser_factory import BrowserFactory


@pytest.fixture(scope="function")
def setup_teardown():
    factory = BrowserFactory()
    driver = factory.get_driver()
    yield driver
    factory.close_driver()
