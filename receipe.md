# Single Table Design Recipe Template


## 1. Extract nouns from the user stories or specification

```
As a book lover,
So I can organise my books,
I want to keep a list of book' titles and authors.

```

```
Nouns:

book, title, author_name
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------- |
| books                 | title, author |

Name of the table: `books`

Column names: `title`, `author_namer`

## 3. Decide the column types


```

id: SERIAL
title: text
author_name: text
```

## 4. Write the SQL

```sql

-- file: book_store.sql

CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  title text,
  author_name text
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 book_store < book_store.sql
```






# Books Model and Repository Classes Design Recipe


## 1. Design and create the Table

```

Table: books

Columns:
id | title | author_name
```

## 2. Create Test SQL seeds

'''Not needed for this challenge'''

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# EXAMPLE
# Table name: books

# Model class
# (in lib/book.py)
class Book


# Repository class
# (in lib/book_repository.py)
class BookRepository

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# EXAMPLE
# Table name: books

# Model class
# (in lib/book.py)

class Book:
    def __init__(self, id, title, author_name):
        self.id = id
        self.title = title
        self.author_name = author_name

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"{self.id} - {self.title} - {self.author_name}"

```


```python
# Test EXAMPLE
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

```

## 5. Define the Repository Class interface

```python

class BookRepository:
    
    def __init__(self, connection):
        self._connection = connection
    # Selecting all records
    # No arguments

    def all(self):
        # Executes the SQL query:
        # SELECT id, title, author_name;

        # Returns an array of Book objects.

        # Gets a single record by its ID
        # One argument: the id (number)


```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# EXAMPLES

def test_get_all_books(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)
    all_books = repository.all()
    assert all_books == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton')
    ]
```



## 7. Test-drive and implement the Repository class behaviour
