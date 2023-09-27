# _*_ coding: utf-8 _*_
from flask import Flask
# config import
from config import app_config, app_active

config = app_config[app_active]

from flask_sqlalchemy import SQLAlchemy

def create_app(config_name):
    app = Flask(__name__, template_folder='templates')
    app.config.from_pyfile('config.py')

    config_object = app_config[config_name]
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SALALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(config.APP)
    db.init_app(app)


    if config_object is None:
        raise Exception('No configuration found for the current environment.')

    app.secret_key = config_object.SECRET
    app.config.from_object(config_object)

    @app.route('/')
    def index():
        return 'hello world'

    return app