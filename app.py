from datetime import datetime

from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase

from models import user, blog, post

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "user_profile_page.html",
        name=name,
        date=datetime.now()
    )