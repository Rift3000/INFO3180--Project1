from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "whatPassword?"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://djcviaztdjzsxe:102ffe4635fe1f75902016e471af8a06806c75fa5fad98014d9db7114950a533@ec2-34-197-212-240.compute-1.amazonaws.com:5432/dsgnh8rsq3vnu"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

UPLOAD_FOLDER = './app/static/uploads'

username = "Thriller"  #Not wise as far as security is concerned but I simply wanted to state the username
password = "cakesoap"  #And the password I used for my database
db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views
