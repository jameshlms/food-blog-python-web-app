from datetime import datetime
from uuid import uuid1

from flask import Flask, request, render_template
import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase

from models.user import User

from service_account_key import ServiceAccountKey

# Use a service account. serv
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

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('sign_up_page.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    user: dict = auth.create_user_with_email_and_password(email, password)
    user_uid: str = user["localId"]

    doc_ref = db.collection("users").document()
    doc_id = doc_ref.id
    user = User(username, email, datetime.now(), "", doc_id, user_uid, [], "", [], [])
    data = user.__dict__
    print(data)
    doc_ref.set(data)

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    username : str = input("Enter a username: ")
    email : str = input("Enter an email: ")
    password : str = input("Enter a password")

    user: dict = auth.create_user_with_email_and_password(email, password)
    user_uid: str = user["localId"]

    doc_ref = db.collection("users").document()
    doc_id = doc_ref.id
    user = User(username, email, datetime.now(), "brwblwghrougblbwlefbkwg", doc_id, user_uid, [], "", [], [])
    data = user.__dict__
    print(data)
    doc_ref.set(data)
    return render_template(
        "user_profile_page.html",
        name=name,
        date=datetime.now()
    )
