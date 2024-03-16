from datetime import datetime

from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase

from models.user import User

from service_account_key import ServiceAccountKey

# Use a service account.
service_account_key = ServiceAccountKey()
cred = credentials.Certificate(service_account_key.key)
app = firebase_admin.initialize_app(cred)
db = firestore.client()

firebase_config : dict = {
    
}

pyrebase_app = pyrebase.initialize_app(firebase_config)
auth = pyrebase_app.auth()

app = Flask(__name__)

def add_user_in_firestore():
    username : str = input("Enter a username: ")
    email : str = input("Enter an email: ")
    password : str = input("Enter a password")


@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    doc_ref = db.collection("users").document()
    doc_id = doc_ref.id
    user = User(name, "tiffxnycho", datetime.now(), "www.instagram.com", doc_id, [], "18", [])
    data = user.__dict__
    doc_ref.set(data)
    return render_template(
        "user_profile_page.html",
        name=name,
        date=datetime.now()
    )