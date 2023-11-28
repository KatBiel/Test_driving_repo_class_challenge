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