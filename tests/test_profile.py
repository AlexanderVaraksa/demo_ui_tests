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

# def test_profile_add_book(login_to_book_store):
#     # WHEN
#     profile_page.click_book_store_menu()
#     books_page.click_book('Git Pocket Guide')
#     books_page.verify_book_properties_page_opened()
#     books_page.click_add_to_your_collection_button()
#     # THEN
#     books_page.verify_alert_text_and_accept('Book added to your collection.')
#     profile_page.click_profile_menu()
#     books_page.verify_book_titles('Git Pocket Guide')
