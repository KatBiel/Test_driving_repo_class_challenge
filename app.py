from lib.database_book_store import DatabaseConnection
from lib.book_repository import *



# Connect to the database
connection = DatabaseConnection()
connection.connect()
connection.seed("seeds/book_store.sql")

Book_repository = BookRepository(connection)

for book in Book_repository.all():
    print(book)

