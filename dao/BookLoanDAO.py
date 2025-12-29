from database import Database
from datetime import date

class BookLoanDAO:
    def __init__(self):
        self.connection = Database().get_connection()

    def get_all_loans(self):
        cursor = self.connection.cursor()
        cursor.execute("""
               select bl.id, r.first_name, r.surname, b.book_name, bl.loan_date, bl.due_date, bl.return_date, bl.loan_state
               from book_loans bl
               join readers r on bl.reader_id = r.id
               join books b on bl.book_id = b.id
           """)
        return cursor.fetchall()

    def get_loan_by_id(self, loan_id):
        cursor = self.connection.cursor()
        cursor.execute("""
                  select bl.id, r.first_name, r.surname, b.book_name, bl.loan_date, bl.due_date, bl.return_date, bl.loan_state
                  from book_loans bl
                  join readers r on bl.reader_id = r.id
                  join books b on bl.book_id = b.id
                  where bl.id = ?
              """, (loan_id,))
        return cursor.fetchone()

    def create_loan(self, reader_id, book_id, loan_days=14):
        cursor = self.connection.cursor()
        try:
            self.connection.autocommit = False

            cursor.execute("select is_available from books where id = ?", book_id)
            row = cursor.fetchone()
            if not row or not row.is_available:
                raise Exception("Book is not available")

            today = date.today()
            due = date.today().replace(day=today.day + loan_days)
            cursor.execute("""
                           insert into book_loans (loan_date, due_date, return_date, loan_state, reader_id, book_id)
                           values (?, ?, ?, 'active', ?, ?)
                       """, today, due, None, reader_id, book_id)

            cursor.execute("update books set is_available = 0 where id = ?", book_id)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            raise e
        finally:
            self.connection.autocommit = True

    def return_loan(self, loan_id):
        cursor = self.connection.cursor()
        try:
            self.connection.autocommit = False

            cursor.execute("select book_id from book_loans where id = ?", loan_id)
            row = cursor.fetchone()
            if not row:
                raise Exception("Book loan not found")
            book_id = row.book_id

            cursor.execute("""
                           update book_loans
                           set return_date = ?, loan_state = 'returned'
                           where id = ?
                       """, date.today(), loan_id)

            cursor.execute("update books set is_available = 1 where id = ?", book_id)

            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            raise e
        finally:
            self.connection.autocommit = True

    def delete_loan(self, loan_id):
        cursor = self.connection.cursor()
        try:
            self.connection.autocommit = False

            cursor.execute("select book_id, loan_state from book_loans where id = ?", loan_id)
            row = cursor.fetchone()
            if not row:
                raise Exception("Book loan not found")
            book_id = row.book_id
            loan_state = row.loan_state

            if loan_state == 'active':
                cursor.execute("update books set is_available = 1 where id = ?", book_id)

            cursor.execute("delete from book_loans where id = ?", loan_id)

            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            raise e
        finally:
            self.connection.autocommit = True