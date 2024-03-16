from datetime import datetime as dt

class Post:
    def __init__(self, header : str, author : str, rating : float, date_created : dt, date_updated : dt, instructions : str, description : str, ingredients : str, doc_id : str, owner_uid : str):
        self.header = header
        self.author = author
        self.rating = rating
        self.date_created = date_created
        self.date_updated = date_updated
        self.instructions = instructions
        self.description = description
        self.ingredients = ingredients
        self.doc_id = doc_id
        self.owner_uid = owner_uid

    