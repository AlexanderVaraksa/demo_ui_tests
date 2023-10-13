from demo_ui_tests.pages.login_page import LoginPage
from demo_ui_tests.constants import user_password, user_name

login_page = LoginPage()


def test_login():
    # GIVEN
    login_page.open()
    # WHEN
    login_page.fill_user_name(user_name)
    login_page.fill_password(user_password)
    login_page.click_login()
    # THEN
    login_page.verify_profile_url_open()
    login_page.verify_user_label()


def test_login_with_wrong_password():
    # GIVEN
    login_page.open()
    # WHEN
    login_page.fill_user_name(user_name)
    login_page.fill_password('123')
    login_page.click_login()
    # THEN
    login_page.verify_error_messge()
