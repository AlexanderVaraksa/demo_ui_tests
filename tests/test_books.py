from selene import browser

from demo_ui_tests.pages.books_page import BooksPage

# books_page = BooksPage()


def test_search_book_by_title():
    books_page = BooksPage()
    books_page.open()
    books_page.verify_book_titles('Git Pocket Guide', 'Learning JavaScript Design Patterns',
                                  'Designing Evolvable Web APIs with ASP.NET',
                                  'Speaking JavaScript', "You Don't Know JS",
                                  'Programming JavaScript Applications',
                                  'Eloquent JavaScript, Second Edition',
                                  'Understanding ECMAScript 6')
    books_page.input_search_text('Java')
    books_page.verify_book_titles(('Learning JavaScript Design Patterns',
                                   'Speaking JavaScript',
                                   'Programming JavaScript Applications',
                                   'Eloquent JavaScript, Second Edition'))
