import pytest
from selene import browser

from demo_ui_tests.constants import base_url_value, user_name, user_password
from demo_ui_tests.pages.login_page import LoginPage

base_url = base_url_value


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.config.base_url = base_url
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 8

    yield

    browser.quit()


@pytest.fixture(scope="function", autouse=False)
def login_to_book_store(login=user_name, password=user_password):
    login_page = LoginPage()
    # GIVEN
    login_page.open()
    login_page.fill_user_name(login)
    login_page.fill_password(password)
    login_page.click_login()
    # login_page.verify_profile_url_open()
    login_page.verify_profile_page_open()

# @pytest.fixture(scope='function', autouse=True)
# def browser_open():
#     browser.config.base_url = base_url
#     browser.config.window_width = 1920
#     browser.config.window_height = 1080
#     # sleep(5)
#     browser.open(base_url)
#
#     yield
#
#     browser.quit()
