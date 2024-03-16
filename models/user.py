from datetime import datetime as dt

class User:
    """
    Represents a user profile.

    Attributes:
        name (str): The full name of the user.
        username (str): The user's chosen username.
        date_created (datetime): The date the user was created.
        image_url (str): URL to the user's profile image.
        uid (str): The unique identifier for the user.
        viewers (list): List of viewers of the user's profile.
        description (str): A brief description of the user.
        tags (list): Tags associated with the user.
    """
    
    def __init__(self, name: str, username: str, date_created: dt, 
                 image_url: str, uid: str, viewers: list, 
                 description: str, tags: list):
        """
        Constructs all the necessary attributes for the user object.

        Parameters:
            name (str): The full name of the user.
            username (str): The user's chosen username.
            date_created (datetime): The date the user was created.
            image_url (str): URL to the user's profile image.
            uid (str): The unique identifier for the user.
            viewers (list): List of viewers of the user's profile.
            description (str): A brief description of the user.
            tags (list): Tags associated with the user.
        """
        self.name = name
        self.username = username
        self.date_created = date_created
        self.image_url = image_url
        self.uid = uid
        self.viewers = viewers
        self.description = description
        self.tags = tags

    def modify_name(self, new_name: str):
        """
        Changes the user's name.

        Parameters:
            new_name (str): The new name to assign to the user.
        """
        self.name = new_name

    def modify_username(self, new_username: str):
        """
        Changes the user's username.

        Parameters:
            new_username (str): The new username to assign to the user.
        """
        self.username = new_username

    def modify_viewers(self, new_viewers: list):
        """
        Updates the list of viewers.

        Parameters:
            new_viewers (list): The new list of viewers to assign to the user.
        """
        self.viewers = new_viewers

    def modify_description(self, new_description: str):
        """
        Updates the user's description.

        Parameters:
            new_description (str): The new description to assign to the user.
        """
        self.description = new_description
