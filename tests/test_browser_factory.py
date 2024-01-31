# test_browser_factory.py
from elements.browser_factory import BrowserFactory


def test_browser_open_close():
    browser_factory = BrowserFactory()
    driver = browser_factory.get_driver()
    assert driver is not None, "Browser is not opened"
    browser_factory.close_driver()
    assert browser_factory._instance.driver is None, "Browser is not closed"
