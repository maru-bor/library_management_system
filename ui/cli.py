from dao.BookDAO import BookDAO
from dao.BookLoanDAO import BookLoanDAO
from ui.menu_item import MenuItem

class ConsoleUI:
    def __init__(self):
        self.book_dao = BookDAO()
        self.loan_dao = BookLoanDAO()

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

    def exit_app(self):
        print("Ending program")
        exit()