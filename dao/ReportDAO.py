from database import Database

class ReportDAO:
    def __init__(self):
        self.connection = Database().get_connection()

    def get_books_view(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "select * from view_books_detail"
        )
        return cursor.fetchall()

    def get_loans_view(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "select * from view_loans_detail"
        )
        return cursor.fetchall()

    def get_book_and_loan_count_by_genre(self):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            select
                g.gen_name,
                count(distinct b.id),
                count(bl.id)
            from genres g
            left join books b on g.id = b.genre_id
            left join book_loans bl on b.id = bl.book_id
            group by g.gen_name
            """
        )
        return cursor.fetchall()

    def get_most_loaned_books(self):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            select top 10
                b.id,
                b.book_name,
                a.first_name + ' ' + a.surname,
                count(bl.id) as loan_count
            from books b
            join authors a on b.author_id = a.id
            join book_loans bl on b.id = bl.book_id
            group by b.id, b.book_name, a.first_name, a.surname
            order by loan_count desc
            """
        )
        return cursor.fetchall()