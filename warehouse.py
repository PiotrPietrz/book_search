from database import DataBase


class Warehouse(DataBase):
    def __init__(self, title: str = None, author: str = None) -> None:
        self.title = title
        self.author = author
        super().__init__()

    def add_book(self, title, author) -> None:
        """
        Function for adding a book to the database.
        By default, the table for storing the books will be called 'books'.
        If the table doesn't exists it will be created. Otherwise,
        new records are added.
        Returns None
        """
        if not super().table_exists('books'):

            query = f"""
                    CREATE TABLE books (
                        title TEXT,
                        author TEXT
                    );


                    INSERT INTO books
                    VALUES ('{title}', '{author}')
                    """

            try:
                super().query_db(query)
                print('Successfuly created database.')
            except:
                raise Exception(
                    f'Query {query} could not have been processed.')

        else:
            query = f"""
                    INSERT INTO books
                    VALUES ('{title}', '{author}')
                    """

            try:
                super().query_db(query)
                print('Successfuly updated the records.')
            except:
                raise Exception(
                    f'Query {query} could not have been processed.')
