# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active
from model.User import User
from model.Category import Category

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    description = db.Column(db.Text(),nullable=False)
    qtd = db.Column(db.Integer,nullable=True, default=0)
    image = db.Column(db.Text(),nullable=True)
    price = db.Column(db.Numeric(10,2),nullable=False)
    date_created = db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)
    last_updated = db.Column(db.DateTime(6), default=db, onupdate=db.func.current_timestamp(), nullable=True)
    status = db.Column(db.Boolean, default=1, nullable=True)
    user_created = db.Column(db.Integer, db.ForeignKey(User.id),nullable=False)
    category = db.Column(db.Integer, db.ForeignKey(Category.id), nullable=False)