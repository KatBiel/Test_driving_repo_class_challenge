from lib.book import Book

'''When i create a book with the fields title and author_name
they are reflected in the instance properties'''

def test_initializer():
    book = Book(1, 'Life of Pi', 'Yann Martel')
    assert book.id == 1
    assert book.title == 'Life of Pi'
    assert book.author_name == 'Yann Martel'

'''Test equality'''
def test_equality():
    book_1 = Book(1, 'Life of Pi', 'Yann Martel')
    book_2 = Book(1, 'Life of Pi', 'Yann Martel')
    assert book_1 == book_2

''' Test formatter'''
def test_formatter():
    book = Book(1, 'Life of Pi', 'Yann Martel')
    assert str(book) == "1 - Life of Pi - Yann Martel"