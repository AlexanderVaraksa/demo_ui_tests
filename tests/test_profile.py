from demo_ui_tests.pages.books_page import BooksPage
from demo_ui_tests.pages.login_page import LoginPage
from demo_ui_tests.pages.profile_page import ProfilePage

profile_page = ProfilePage()
login_page = LoginPage()
books_page = BooksPage()


def test_profile_logout(login_to_book_store):
    # WHEN
    profile_page.click_log_out_button()
    # THEN
    login_page.verify_login_url_open()
    login_page.verify_login_page_open()


def test_login_page_not_available_for_logged_user(login_to_book_store):
    # WHEN
    profile_page.click_login_menu()
    # THEN
    login_page.verify_login_url_open()
    login_page.verify_login_page_open()
    login_page.verify_you_already_logged_in_text()
