from app.dao.BookDAO import BookDAO
from app.dao.BookLoanDAO import BookLoanDAO
from app.dao.AuthorDAO import AuthorDAO
from app.dao.ReaderDAO import ReaderDAO
from app.dao.GenreDAO import GenreDAO
from app.dao.ReportDAO import ReportDAO
from app.CSVImport import CSVImport
from ui.menu_item import MenuItem
from datetime import datetime

class ConsoleUI:
    def __init__(self):
        self.book_dao = BookDAO()
        self.loan_dao = BookLoanDAO()
        self.author_dao = AuthorDAO()
        self.reader_dao = ReaderDAO()
        self.genre_dao = GenreDAO()
        self.report_dao = ReportDAO()
        self.csv_import = CSVImport(book_dao=self.book_dao,author_dao=self.author_dao)

    def input_non_empty_string(self, prompt):
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("Input cannot be empty.")

    def input_int(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Please enter a valid integer.")

    def input_float(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Please enter a valid number.")

    def input_date(self, prompt):
        while True:
            value = input(prompt)
            try:
                datetime.strptime(value, "%Y-%m-%d")
                return value
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")

    def run_menu(self, title, menu_items):
        while True:
            print(f"\n=== {title} ===")
            for item in menu_items:
                print(f"{item.key} - {item.description}")

            choice = input("Choice: ")

            for item in menu_items:
                if item.key == choice:
                    item.execute()
                    if item.action.__name__ in ("main_menu",):
                        return

                    break

            else:
                print("Invalid choice")

    def main_menu(self):
        menu_items = [
            MenuItem("1", "Manage book loans", self.book_loans_menu),
            MenuItem("2", "Manage books", self.books_menu),
            MenuItem("3", "Manage authors", self.authors_menu),
            MenuItem("4", "Manage readers (users)", self.readers_menu),
            MenuItem("5", "Manage genres", self.genres_menu),
            MenuItem("6", "View library statistics (views + reports)", self.reports_menu),
            MenuItem("7", "Import data from CSV file", self.import_data_menu),
            MenuItem("0", "End program", self.exit_app)
        ]
        self.run_menu("Library Management System", menu_items)

    def books_menu(self):
        menu_items = [
            MenuItem("1", "Show all books", self.show_books),
            MenuItem("2", "Add new book", self.add_book),
            MenuItem("3", "Delete book", self.delete_book),
            MenuItem("0", "Back", self.main_menu)
        ]
        self.run_menu("Books", menu_items)

    def book_loans_menu(self):
        menu_items = [
            MenuItem("1", "Show all loans", self.show_loans),
            MenuItem("2", "Add new loan", self.add_loan),
            MenuItem("3", "Return book", self.return_loan),
            MenuItem("4", "Update loan", self.update_loan),
            MenuItem("5", "Delete loan", self.delete_loan),
            MenuItem("0", "Back", self.main_menu)
        ]
        self.run_menu("Book Loans", menu_items)

    def authors_menu(self):
        menu_items = [
            MenuItem("1", "Show all authors", self.show_authors),
            MenuItem("2", "Add author", self.add_author),
            MenuItem("3", "Delete author", self.delete_author),
            MenuItem("0", "Back", self.main_menu)
        ]
        self.run_menu("Authors", menu_items)

    def readers_menu(self):
        menu_items = [
            MenuItem("1", "Show all readers", self.show_readers),
            MenuItem("2", "Add reader", self.add_reader),
            MenuItem("3", "Delete reader", self.delete_reader),
            MenuItem("0", "Back", self.main_menu)
        ]
        self.run_menu("Readers", menu_items)

    def genres_menu(self):
        menu_items = [
            MenuItem("1", "Show all genres", self.show_genres),
            MenuItem("2", "Add genre", self.add_genre),
            MenuItem("3", "Delete genre", self.delete_genre),
            MenuItem("0", "Back", self.main_menu)
        ]
        self.run_menu("Genres", menu_items)

    def reports_menu(self):
        menu_items = [
            MenuItem("1", "Books overview (view)", self.show_books_view),
            MenuItem("2", "Loans overview (view)", self.show_loans_view),
            MenuItem("3", "Book and loan count by genre", self.show_genre_statistics),
            MenuItem("4", "Most Borrowed Books (top 10)", self.show_most_borrowed_books),
            MenuItem("0", "Back", self.main_menu)
        ]
        self.run_menu("Library Statistics (views + reports)", menu_items)

    def import_data_menu(self):
        menu_items = [
            MenuItem("1", "Import books from CSV file", self.import_books),
            MenuItem("2", "Import authors from CSV file", self.import_authors),
            MenuItem("0", "Back", self.main_menu)
        ]
        self.run_menu("Import Data", menu_items)

    # Books - functions
    def show_books(self):
        try:
            books = self.book_dao.get_all_books()
            print("\nBOOK ID | BOOK NAME | PUBLISH DATE | PRICE | IS AVAILABLE | AUTHOR ID | GENRE ID")
            for book in books:
                print(book)
        except Exception as e:
            print("Error while fetching books:", e)


    def add_book(self):
        try:
            name = self.input_non_empty_string("Name of book: ")
            publish_date = self.input_date("Publish date (YYYY-MM-DD): ")
            price = self.input_float("Price: ")
            author_id = self.input_int("Author ID: ")
            genre_id = self.input_int("Genre ID: ")

            if price <= 0:
                raise ValueError("Price must be greater than 0")

            self.book_dao.create_book(name, publish_date, price, author_id, genre_id)
            print("Book added.")
        except Exception as e:
            print("Error while adding book:", e)

    def delete_book(self):
        book_id = self.input_int("Book ID: ")

        try:
            self.book_dao.delete_book(book_id)
            print("Book deleted.")
        except Exception as e:
            print("Error:", e)

    # Book loans - functions
    def show_loans(self):
        try:
            loans = self.loan_dao.get_all_loans()
            print("\nLOAN ID | READER FIRST NAME | READER SURNAME | BOOK NAME | LOAN DATE | DUE DATE | RETURN DATE | LOAN STATE")
            for loan in loans:
                print(loan)
        except Exception as e:
            print("Error while loading loans:", e)


    def add_loan(self):
        reader_id = self.input_int("Reader ID: ")
        book_id = self.input_int("Book ID: ")

        try:
            self.loan_dao.create_loan(reader_id, book_id)
            print("Loan created.")
        except Exception as e:
            print("Error while creating loan:", e)


    def return_loan(self):
        loan_id = self.input_int("Loan ID: ")

        try:
            self.loan_dao.return_loan(loan_id)
            print("Book returned.")
        except Exception as e:
            print("Error while returning book:", e)

    def update_loan(self):
        try:
            loan_id = self.input_int("Loan ID: ")
            new_due_date_str = self.input_date("New due date (YYYY-MM-DD): ")
            new_state = self.input_non_empty_string("New loan state (active/returned): ").lower()

            if new_state not in ("active", "returned"):
                print("Invalid loan state")
                return

            self.loan_dao.update_loan(loan_id, new_due_date_str, new_state)
            print("Loan updated.")

        except ValueError as e:
            print("Input error:", e)
        except Exception as e:
            print("Error while updating loan:", e)


    def delete_loan(self):
        loan_id = self.input_int("Loan ID: ")

        try:
            self.loan_dao.delete_loan(loan_id)
            print("Loan deleted.")
        except Exception as e:
            print("Error while deleting loan:", e)



    # Authors - functions
    def show_authors(self):
        try:
            authors = self.author_dao.get_all_authors()
            print("\nAUTHOR ID | FIRST NAME | SURNAME")
            for a in authors:
                print(a)
        except Exception as e:
            print("Error:", e)


    def add_author(self):
        first_name = self.input_non_empty_string("First name: ")
        surname = self.input_non_empty_string("Surname: ")

        try:
            self.author_dao.create_author(first_name, surname)
            print("Author created.")
        except Exception as e:
            print("Error:", e)


    def delete_author(self):
        author_id = self.input_int("Author ID: ")

        try:
            self.author_dao.delete_author(author_id)
            print("Author deleted.")
        except Exception as e:
            print("Error:", e)

    # Readers - functions
    def show_readers(self):
        try:
            readers = self.reader_dao.get_all_readers()
            print("\nREADER ID | FIRST NAME | SURNAME | EMAIL")
            for r in readers:
                print(r)
        except Exception as e:
            print("Error:", e)


    def add_reader(self):
        first_name = self.input_non_empty_string("First name: ")
        surname = self.input_non_empty_string("Surname: ")
        email = self.input_non_empty_string("Email: ")

        try:
            self.reader_dao.create_reader(first_name, surname, email)
            print("Reader created.")
        except Exception as e:
            print("Error:", e)


    def delete_reader(self):
        reader_id = self.input_int("Reader ID: ")

        try:
            self.reader_dao.delete_reader(reader_id)
            print("Reader deleted.")
        except Exception as e:
            print("Error:", e)

    # Genres - functions
    def show_genres(self):
        try:
            genres = self.genre_dao.get_all_genres()
            print("\nGENRE ID | GENRE NAME")
            for g in genres:
                print(g)
        except Exception as e:
            print("Error:", e)


    def add_genre(self):
        name = self.input_non_empty_string("Genre name: ")

        try:
            self.genre_dao.create_genre(name)
            print("Genre created.")
        except Exception as e:
            print("Error:", e)


    def delete_genre(self):
        genre_id = self.input_int("Genre ID: ")

        try:
            self.genre_dao.delete_genre(genre_id)
            print("Genre deleted.")
        except Exception as e:
            print("Error:", e)


    # Library Statistics - functions
    def show_books_view(self):
        try:
            rows = self.report_dao.get_books_view()
            print("\nBOOK ID | BOOK NAME | AUTHOR NAME | GENRE NAME | PRICE | IS AVAILABLE")
            for row in rows:
                print(row)
        except Exception as e:
            print("Error:", e)

    def show_loans_view(self):
        try:
            rows = self.report_dao.get_loans_view()
            print("\nLOAN ID | READER NAME | BOOK NAME | LOAN DATE | DUE DATE | RETURN DATE | LOAN STATE ")
            for row in rows:
                print(row)
        except Exception as e:
            print("Error:", e)

    def show_genre_statistics(self):
        try:
            rows = self.report_dao.get_genre_statistics()
            print("\nGENRE STATISTICS")
            print("GENRE NAME | BOOK COUNT | LOAN COUNT")

            for row in rows:
                print(row)
        except Exception as e:
            print("Error:", e)

    def show_most_borrowed_books(self):
        try:
            rows = self.report_dao.get_most_borrowed_books()
            print("\nTOP 10 MOST BORROWED BOOKS")
            print("BOOK ID | BOOK NAME | AUTHOR NAME | LOAN COUNT")
            for row in rows:
                print(row)
        except Exception as e:
            print("Error:", e)

    # CSV Import - functions
    def import_books(self):
        print("!! The CSV file must first be in the project root directory BEFORE importing it !!")
        filename = input("Enter CSV filename: ")
        try:
            self.csv_import.import_books_from_csv(filename)
        except Exception as e:
            print("Import failed:", e)

    def import_authors(self):
        print("!! The CSV file must first be in the project root directory BEFORE importing it !!")
        filename = input("Enter CSV filename: ")
        try:
            self.csv_import.import_authors_from_csv(filename)
        except Exception as e:
            print("Import failed:", e)



    def exit_app(self):
        print("Ending program")
        exit()