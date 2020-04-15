from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "whatPassword?"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://zbkbqvbcoxxbfc:182cb67a653e37f966d2ceff0809d227d5032f6eddc503944d80cd8500c046e7@ec2-18-210-51-239.compute-1.amazonaws.com:5432/dduqt5vmln98qm"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

UPLOAD_FOLDER = './app/static/uploads'

username = "Thriller"  #Not wise as far as security is concerned but I simply wanted to state the username
password = "cakesoap"  #And the password I used for my database
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

app.config.from_object(__name__)
from app import views
