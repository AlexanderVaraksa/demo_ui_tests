from time import sleep

import pytest
from selene import browser

base_url = 'https://demoqa.com/books'


@pytest.fixture(scope='function', autouse=True)
def browser_open():
    browser.config.base_url = base_url
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    # sleep(5)
    # browser.open(base_url)

    yield

    browser.quit()
