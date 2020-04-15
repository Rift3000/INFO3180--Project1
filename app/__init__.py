from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "whatPassword?"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://zaqahrusiorfbg:70fd98a0a9f2d3b93f020545305019480877a9974e46ca7d9653f41f672b18a7@ec2-52-87-58-157.compute-1.amazonaws.com:5432/d5kuns2vecqunb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

UPLOAD_FOLDER = './app/static/uploads'

username = "Thriller"  #Not wise as far as security is concerned but I simply wanted to state the username
password = "cakesoap"  #And the password I used for my database
db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views
