from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import redis

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'abcdefgh45gsdi4934jdfkn4134ua430gnjnes84' 
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True 
app.config['MAIL_USERNAME'] = 'sssa.aditi@gmail.com'
app.config['MAIL_PASSWORD'] = 'Your_Password'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB.db'

db = SQLAlchemy(app)  
redis_cli = redis.Redis(host="localhost", port=6379, db=0)
