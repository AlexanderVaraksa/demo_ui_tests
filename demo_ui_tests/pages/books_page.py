import allure
from selene import browser, have


class BooksPage:

    def open(self):
        browser.open('/books')
        # browser.driver.execute_script("$('footer').remove()")
        # browser.driver.execute_script("$('#fixedban').remove()")
        # return self

    def verify_book_titles(self, *titles):
        with allure.step(f'Verify books titles: {titles}'):
            browser.all('[id^=see-book]').should(
                have.exact_texts(titles))

    def input_search_text(self, search_string):
        with allure.step(f'Search book with keyword: {search_string}'):
            browser.element('#searchBox').type(search_string)

    def click_book(self, book_title):
        with allure.step(f'Click book title: {book_title}'):
            browser.all('[id^=see-book]').element_by(have.exact_text(book_title)).click()

    def verify_no_books_found(self):
        with allure.step(f'Verify no books shown'):
            browser.element('.rt-noData').should(have.exact_text('No rows found'))