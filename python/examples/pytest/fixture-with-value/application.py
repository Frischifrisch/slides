class App:
    def __init__(self):
        self.pi = 3.14
        # .. set up database
        print("__init__ of App")


    def add_user(self, name):
        print(f"Working on add_user({name})")
        self.name = name

    def get_user(self):
        return self.name
