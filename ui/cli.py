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
                    return

            print("invalid choice")