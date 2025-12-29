from database import Database

class GenreDAO:
    def __init__(self):
        self.connection = Database().get_connection()

    def get_all_genres(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "select id, gen_name from genres"
        )
        return cursor.fetchall()

    def get_genre_by_id(self, genre_id):
        cursor = self.connection.cursor()
        cursor.execute(
            "select id, gen_name from genres where id = ?",
            genre_id
        )
        return cursor.fetchone()

    def create_genre(self, gen_name):
        cursor = self.connection.cursor()
        cursor.execute(
            "insert into genres (gen_name) values (?)",
            gen_name
        )
        self.connection.commit()

    def delete_genre(self, genre_id):
        cursor = self.connection.cursor()
        cursor.execute(
            "delete from genres where id = ?",
            genre_id
        )
        self.connection.commit()