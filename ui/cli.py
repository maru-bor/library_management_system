from dao.BookDAO import BookDAO
from dao.BookLoanDAO import BookLoanDAO
from dao.AuthorDAO import AuthorDAO
from dao.ReaderDAO import ReaderDAO
from dao.GenreDAO import GenreDAO
from ui.menu_item import MenuItem
from datetime import datetime

class ConsoleUI:
    def __init__(self):
        self.book_dao = BookDAO()
        self.loan_dao = BookLoanDAO()
        self.author_dao = AuthorDAO()
        self.reader_dao = ReaderDAO()
        self.genre_dao = GenreDAO()

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

            choice = input("choice: ")

            for item in menu_items:
                if item.key == choice:
                    item.execute()
                    if item.action.__name__ in ("main_menu",):
                        return

                    break

            else:
                print("invalid choice")

    def main_menu(self):
        menu_items = [
            MenuItem("1", "Book loans", self.book_loans_menu),
            MenuItem("2", "Books", self.books_menu),
            MenuItem("3", "Authors", self.authors_menu),
            MenuItem("4", "Readers (Users)", self.readers_menu),
            MenuItem("5", "Genres", self.genres_menu),
            MenuItem("0", "End program", self.exit_app)
        ]
        self.run_menu("Library Management System", menu_items)

    def books_menu(self):
        menu_items = [
            MenuItem("1", "Show all books", self.show_books),
            MenuItem("2", "Add new book", self.add_book),
            MenuItem("0", "Back", self.main_menu)
        ]
        self.run_menu("books", menu_items)

    def book_loans_menu(self):
        menu_items = [
            MenuItem("1", "Show all loans", self.show_loans),
            MenuItem("2", "Create new loan", self.add_loan),
            MenuItem("3", "Return book", self.return_loan),
            MenuItem("4", "Delete loan", self.delete_loan),
            MenuItem("0", "Back", self.main_menu)
        ]
        self.run_menu("book loans", menu_items)

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

    def show_books(self):
        books = self.book_dao.get_all_books()
        for book in books:
            print(book)

    def add_book(self):
        name = input("name of book: ")
        publish_date = input("publish date (yyyy-mm-dd): ")
        price = float(input("price: "))
        author_id = int(input("author ID: "))
        genre_id = int(input("genre ID: "))

        self.book_dao.create_book(name, publish_date, price, author_id, genre_id)
        print("Book added successfully")

    def show_loans(self):
        loans = self.loan_dao.get_all_loans()
        for loan in loans:
            print(loan)

    def add_loan(self):
        reader_id = int(input("reader ID: "))
        book_id = int(input("book ID: "))

        try:
            self.loan_dao.create_loan(reader_id, book_id)
            print("Loan created successfully")
        except Exception as e:
            print("Error while creating loan:", e)

    def return_loan(self):
        loan_id = int(input("Loan ID: "))

        try:
            self.loan_dao.return_loan(loan_id)
            print("Book returned successfully")
        except Exception as e:
            print("Error while returning book:", e)

    def delete_loan(self):
        loan_id = int(input("Loan ID: "))

        try:
            self.loan_dao.delete_loan(loan_id)
            print("Loan deleted successfully")
        except Exception as e:
            print("Error while deleting loan:", e)



    def show_authors(self):
        try:
            authors = self.author_dao.get_all_authors()
            for a in authors:
                print(a)
        except Exception as e:
            print("Error:", e)


    def add_author(self):
        first_name = self.input_non_empty_string("First name: ")
        surname = self.input_non_empty_string("Surname: ")

        try:
            self.author_dao.create_author(first_name, surname)
            print("Author successfully created.")
        except Exception as e:
            print("Error:", e)


    def delete_author(self):
        author_id = self.input_int("Author ID: ")

        try:
            self.author_dao.delete_author(author_id)
            print("Author successfully deleted.")
        except Exception as e:
            print("Error:", e)

    def show_readers(self):
        try:
            readers = self.reader_dao.get_all_readers()
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

    def show_genres(self):
        try:
            genres = self.genre_dao.get_all_genres()
            for g in genres:
                print(g)
        except Exception as e:
            print("Error:", e)

        input("Press enter to continue...")

    def add_genre(self):
        name = self.input_non_empty_string("Genre name: ")

        try:
            self.genre_dao.create_genre(name)
            print("Genre created.")
        except Exception as e:
            print("Error:", e)

        input("Press enter to continue...")

    def delete_genre(self):
        genre_id = self.input_int("Genre ID: ")

        try:
            self.genre_dao.delete_genre(genre_id)
            print("Genre deleted.")
        except Exception as e:
            print("Error:", e)

        input("Press enter to continue...")


    def exit_app(self):
        print("Ending program")
        exit()