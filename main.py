from ui.cli import ConsoleUI


def main():
    try:
        app = ConsoleUI()
        app.main_menu()
    except RuntimeError as e:
        print(e)


if __name__ == "__main__":
    main()