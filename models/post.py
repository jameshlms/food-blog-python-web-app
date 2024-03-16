from datetime import datetime as dt

class Post:
    def __init__(self, header : str, author : str, date_created : dt, date_updated : dt, recipe : str, instructions : str, description : str):
        self.header = header
        self.author = author
        self.date_created = date_created
        self.date_updated = date_updated
        self.recipe = recipe
        self.description = description

    