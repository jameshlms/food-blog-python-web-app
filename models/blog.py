from datetime import datetime as dt

class Blog:
    def __init__(self, nickname : str, posts : list, followers : list, last_upadated : dt, date_created : dt):
        self.nickname : str = nickname
        self.posts : int = posts
        self.followers : int = followers
        self.last_updated : dt = last_upadated
        self.date_created : dt = date_created

    def __init__(self, nickname : str, date_created : dt):
        self.nickname : str = nickname
        self.posts : int = 0
        self.followers : int = 0
        self.last_updated : dt = date_created
        self.date_created : dt = date_created

    def modify_nickname(self, new_nickname : str):
        self.nickname : str = new_nickname