from db.database import Database

class AuthorDAO:
    def __init__(self):
        self.connection = Database().get_connection()

    def get_all_authors(self):
        cursor = self.connection.cursor()
        cursor.execute("select id, first_name, surname from authors")
        return cursor.fetchall()

    def get_author_by_id(self, author_id):
        cursor = self.connection.cursor()
        cursor.execute(
            "select id, first_name, surname from authors where id = ?",
            author_id
        )
        return cursor.fetchone()

    def create_author(self, first_name, surname):
        cursor = self.connection.cursor()
        cursor.execute(
            "insert into authors (first_name, surname) values (?, ?)",
            first_name, surname
        )
        self.connection.commit()

    def delete_author(self, author_id):
        cursor = self.connection.cursor()
        cursor.execute(
            "delete from authors where id = ?",
            author_id
        )
        if cursor.rowcount == 0:
            raise ValueError("Author with given ID does not exist")
        self.connection.commit()