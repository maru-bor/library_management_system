class MenuItem:
    def __init__(self, key, description, action):
        self.key = key
        self.description = description
        self.action = action

    def execute(self):
        self.action()