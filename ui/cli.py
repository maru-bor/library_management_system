from dao.BookDAO import BookDAO
from ui.menu_item import MenuItem

class ConsoleUI:
    def __init__(self):
        self.book_dao = BookDAO()

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
            MenuItem("1", "books", self.books_menu),
            MenuItem("0", "end program", self.exit_app)
        ]
        self.run_menu("Library Management System", menu_items)

    def books_menu(self):
        menu_items = [
            MenuItem("1", "show all books", self.show_books),
            MenuItem("2", "add new book", self.add_book),
            MenuItem("0", "back", self.main_menu)
        ]
        self.run_menu("books", menu_items)

    def show_books(self):
        books = self.book_dao.get_all()
        for book in books:
            print(book)

    def add_book(self):
        name = input("name of book: ")
        publish_date = input("publish date (yyyy-mm-dd): ")
        price = float(input("price: "))
        author_id = int(input("author ID: "))
        genre_id = int(input("genre ID: "))

        self.book_dao.insert_book(name, publish_date, price, author_id, genre_id)
        print("Book added successfully")


    def exit_app(self):
        print("Ending program")
        exit()