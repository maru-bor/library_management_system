from db.database import *

class BookDAO:
    def __init__(self):
        self.connection = Database().get_connection()

    def create_book(self, name, publish_date, price, author_id, genre_id):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            insert into books (book_name, publish_date, price, is_available, author_id, genre_id)
            values (?, ?, ?, 1, ?, ?)
            """,
            name, publish_date, price, author_id, genre_id
        )
        self.connection.commit()

    def get_all_books(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "select id, book_name, publish_date, price, is_available, author_id, genre_id from books"
        )
        return cursor.fetchall()

    def get_book_by_id(self, book_id):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            select id, book_name, publish_date, price, is_available, author_id, genre_id
            from books
            where id = ?
            """,
            book_id
        )
        return cursor.fetchone()

    def delete_book(self, book_id):
        cursor = self.connection.cursor()
        cursor.execute(
            "delete from books where id = ?",
            book_id
        )
        if cursor.rowcount == 0:
            raise ValueError("Book with given ID does not exist")
        self.connection.commit()
