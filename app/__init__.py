from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "whatPassword?"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://postgres:superuser@localhost/Project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

UPLOAD_FOLDER = './app/static/uploads'

username = "Thriller"  #Not wise as far as security is concerned but I simply wanted to state the username
password = "cakesoap"  #And the password I used for my database
db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
