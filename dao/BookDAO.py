from database import *

class BookDAO:
    def __init__(self):
        self.connection = Database().get_connection()

    def insert_book(self, name, publish_date, price, author_id, genre_id):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            insert into books (book_name, publish_date, price, is_available, author_id, genre_id)
            values (?, ?, ?, 1, ?, ?)
            """,
            name, publish_date, price, author_id, genre_id
        )
        self.connection.commit()

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "select id, book_name, price, is_available from books"
        )
        return cursor.fetchall()

