from datetime  import datetime as dt

class User:
    def __init__(self, name : str, username : str, date_created : dt, image_url : str, uid : str, viewers : list, description : str, tags : list):
        self.name : str = name
        self.username : str = username
        self.date_created : dt = date_created
        self.image_url : str = image_url
        self.uid : str = uid
        self.viewers : list = viewers 
        self.description : str = description
        self.tags : list = tags

    def modify_name(self, new_name : str):
        self.name = new_name

    def modify_username(self, new_username : str):
        self.username = new_username

    def modify_viewers(self, new_viewers : list):
        self.viewers = new_viewers

    def modify_description(self, new_description : str):
        self.description = new_description 