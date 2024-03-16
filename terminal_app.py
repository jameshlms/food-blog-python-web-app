from datetime import datetime

import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase

from models.user import User
from models.post import Post

from service_account_key import ServiceAccountKey

# Use a service account.
service_account_key = ServiceAccountKey()
cred = credentials.Certificate(service_account_key.key)
app = firebase_admin.initialize_app(cred)
db = firestore.client()

firebase_config : dict = {
    "apiKey": "AIzaSyCw9pPSkN9hQT9N7-KNWkpn1hxH1A6VBAo",
    "authDomain": "dormroom-delights.firebaseapp.com",
    "projectId": "dormroom-delights",
    "storageBucket": "dormroom-delights.appspot.com",
    "messagingSenderId": "28608723346",
    "appId": "1:28608723346:web:73ff6ada634ee3c628694b",
    "measurementId": "G-RV1K36M957",
    "databaseURL": ""
}

pyrebase_app = pyrebase.initialize_app(firebase_config)
auth = pyrebase_app.auth()

current_username = ""
current_user_uid = ""

def create_user():
    username : str = input("Enter a username:\n> ")
    email : str = input("Enter an email:\n> ")
    password : str = input("Enter a password:\n> ")

    auth_user: dict = auth.create_user_with_email_and_password(email, password)
    user_uid: str = auth_user["localId"]

    doc_ref = db.collection("users").document(user_uid)
    doc_id = doc_ref.id
    user = User(username, email, datetime.now(), "", doc_id, user_uid, [], "", [], [])
    current_username = username
    current_user_uid = user_uid
    data = user.__dict__
    print("Account created!")
    doc_ref.set(data)

def sign_in_user():
    email : str = input("Enter your email:\n> ")
    password : str = input("Enter your password:\n> ")

    auth_user: dict = auth.sign_in_with_email_and_password(email, password)
    current_user_uid: str = auth_user["localId"]

    doc_ref = db.collection('users').document(current_user_uid)
    doc_snapshot = doc_ref.get().to_dict()
    user = User(doc_snapshot['username'], doc_snapshot['email'], doc_snapshot['date_created'], doc_snapshot['image_url'], doc_snapshot['doc_id'], doc_snapshot['user_uid'], doc_snapshot['viewers'], doc_snapshot['description'], doc_snapshot['tags'], doc_snapshot['posts'])
    current_username = user.get_username()
    current_user_uid = user.get_user_uid()
    current_date_created = user.get_date_created()
    print(f'Your username is {current_username} and your account was created on {current_date_created}')
    

def create_post():
    doc_ref = db.collection("posts").document()

    header : str = input("Enter the title of your post: ")
    author : str = current_username
    rating : int = 0
    date_created = datetime.now()
    date_updated = datetime.now()
    instructions = input("Enter instructions for your recipe: ")
    description = input("Enter a description of your food: ")
    ingredients = input("Enter your list of ingredients: ")
    doc_id = doc_ref.id
    owner_uid = current_user_uid
    
    post = Post(header, author, rating, date_created, date_updated, instructions, description, ingredients, doc_id, owner_uid)
    data = post.__dict__
    print(f"Post created! your post id is {doc_id}")
    doc_ref.set(data)

def find_post():
    doc_id = input("Please enter the id of the post you'd like to find:\n> ")
    doc_ref = db.collection('posts').document(doc_id)
    document = doc_ref.get()
    print(document.to_dict())

is_invalid_input : bool = True
should_continue : bool = False

while is_invalid_input is True:
    action = input("Type the action to be performed (for a list of actions, type \'list\'):\n> ")
    if action == 'log in':
        is_invalid_input = False
        should_continue = True
        sign_in_user()
    elif action == 'sign up':
        is_invalid_input = False
        should_continue = True
        create_user()
    elif action == 'quit':
        is_invalid_input = False
        pass
    elif action == 'list':
        is_invalid_input = True
        print('The list of actions are:\n    \'log in\'\n    \'sign up\'\n    \'quit\'')
    else:
        is_invalid_input = True
        print('Please enter a valid action.')

is_invalid_input = True

if should_continue == True:
    while is_invalid_input == True:
        action = input("Please enter your next desired action (enter \'list\' for a list of actions):\n> ")
        if action == 'create post':
            create_post()
        elif action == 'search posts':
            find_post()
            pass
        elif action == 'list':
            print('The list of actions are:\n    \'create post\'\n    \'search posts\'\n    \'quit\'')
        elif action == 'quit':
            is_invalid_input = False
        else:
            print("Please enter a valid input")
        

