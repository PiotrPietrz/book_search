from database import DataBase
from typing import List, Dict


class Warehouse(DataBase):
    def __init__(self, title: str = None, author: str = None, genre: str = None) -> None:
        self.title = title
        self.author = author
        super().__init__()

    def add_book(self, title, author, genre) -> None:
        """
        Function for adding a book to the database.
        By default, the table for storing the books will be called 'books'.
        If the table doesn't exists it will be created. Otherwise,
        new records are added.
        Returns None
        """
        create_table = f"""
                CREATE TABLE books (
                    title TEXT,
                    author TEXT,
                    genre TEXT
                );
                """

        book_add = f"""
                INSERT INTO books
                VALUES ('{title}', '{author}', '{genre}')
                """
        if not super().table_exists("books"):

            try:
                super().query_db(create_table)
                super().query_db(book_add)
                print("Successfuly created database and added records.")
            except:
                raise Exception(
                    f"Either table creation or book insertion has failed.")

        else:
            try:
                super().query_db(book_add)
                print("Successfuly updated the records.")
            except:
                raise Exception(f"Could not add the book.")

    def display(self, title: str = None, author: str = None) -> List[Dict]:
        """
        Function gathering requested data. The data is then passed to jinja for loop
        in the html template.
        Returns a list of dictionaries.
        """

        pass
