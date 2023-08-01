import pytest
from selene.support.shared import browser


@pytest.fixture(autouse=True)
def web_browser():
    browser.config.window_width = 1400
    browser.config.window_height = 1600
    yield
    browser.quit()
