from database import *

class BookDAO:
    def __init__(self):
        self.connection = Database().get_connection()



