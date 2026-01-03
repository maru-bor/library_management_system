import csv

class CSVImport:
    def __init__(self, book_dao, author_dao):
        self.book_dao = book_dao
        self.author_dao = author_dao

    def import_books_from_csv(self, filename):
        try:
            with open(filename, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    try:
                        self.book_dao.create_book(
                            row['book_name'],
                            row['publish_date'],
                            float(row['price']),
                            int(row['author_id']),
                            int(row['genre_id'])
                        )
                    except Exception as e:
                        print(f"Error inserting row {row}: {e}")
            print("Import finished successfully")
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print(f"Error reading file: {e}")


    def import_authors_from_csv(self, filename):
        try:
            with open(filename, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    try:
                        self.author_dao.create_author(
                            row['first_name'],
                            row['surname'],
                        )
                    except Exception as e:
                        print(f"Error inserting row {row}: {e}")
            print("Import finished successfully")
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print(f"Error reading file: {e}")