from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import datetime
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lyxiong:luyuan@localhost:3306/project_db'
db = SQLAlchemy(app)
db.init_app(app)
db.drop_all()
db.create_all()
# db.init_app(app)




class Admin(db.Model):
    __tablename__ = 'admin'
    admin_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)



class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    first_name = db.Column(db.String(15))
    last_name = db.Column(db.String(15))
    gender = db.Column(db.String(11))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(50),nullable=False)
    profile = db.Column(db.String(50))
    hobby = db.Column(db.String(50))
    reg_date = db.Column(db.Date,nullable=False,default=datetime.datetime.now().date())

class Property(db.Model):
    __tablname__ = 'property'
    pro_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    property_type = db.Column(db.String(11))
    state = db.Column(db.String(30))
    city = db.Column(db.String(30))
    address = db.Column(db.String(30))
    zipcode = db.Column(db.Integer())
    owner = db.Column(db.String(30))
    bedroom = db.Column(db.Integer())
    bathroom = db.Column(db.Integer())
    parking = db.Column(db.Integer())

    pets = db.Column(db.Boolean(),default=False)
    # spa = db.Column(db.Boolean(),default=False)
    fitness = db.Column(db.Boolean(),default=False)
    # pool = db.Column(db.Boolean(),default=False)
    wifi  = db.Column(db.Boolean(),default=False)
    img_url = db.Column(db.String(255))
    # air_dryer = db.Column(db.Boolean(),default=False)
    # smoking = db.Column(db.Boolean(),default=False)


class Orders(db.Model):
    __tablname__ = 'order'
    order_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    status = db.Column(db.Integer(), nullable=False, default=0)
    price = db.Column(db.Float(10), nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    description = db.Column(db.String(255))
    tenant = db.Column(db.String(30))
    owner = db.Column(db.String(30), nullable=False)
    property_id = db.Column(db.Integer(),nullable=False)
    ord_date = db.Column(db.Date, nullable=False, default=datetime.datetime.now().date())
    rating = db.Column(db.Float(1))
    review = db.Column(db.String(500))

class Log(db.Model):
    __tablename__ = 'log'
    log_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    client = db.Column(db.Integer())
    content = db.Column(db.Text)
    log_date = db.Column(db.Date, nullable=False, default=datetime.datetime.now().date())

