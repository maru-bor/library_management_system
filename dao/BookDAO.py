from database import *

class BookDAO:
    def __init__(self):
        self.connection = Database().get_connection()

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "select id, book_name, price, is_available from books"
        )
        return cursor.fetchall()

