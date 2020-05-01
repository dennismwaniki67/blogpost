from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SECRET_KEY']= '6b5818f5898dfa22b76c4222a8d5dbe4'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'

db=SQLAlchemy(app)
bcrypt = Bcrypt(app)


from app import views