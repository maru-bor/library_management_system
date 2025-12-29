from database import Database

class ReaderDAO:
    def __init__(self):
        self.connection = Database().get_connection()

    def get_all_readers(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "select id, first_name, surname, email from readers"
        )
        return cursor.fetchall()

    def get_reader_by_id(self, reader_id):
        cursor = self.connection.cursor()
        cursor.execute(
            "select id, first_name, surname, email from readers where id = ?",
            reader_id
        )
        return cursor.fetchone()

    def create_reader(self, first_name, surname, email):
        cursor = self.connection.cursor()
        cursor.execute(
            "insert into readers (first_name, surname, email) values (?, ?, ?)",
            first_name, surname, email
        )
        self.connection.commit()

    def delete_reader(self, reader_id):
        cursor = self.connection.cursor()
        cursor.execute(
            "delete from readers where id = ?",
            reader_id
        )
        self.connection.commit()