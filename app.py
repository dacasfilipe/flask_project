# _*_ coding: utf-8 _*_
from flask import Flask
# config import
from config import app_config, app_active

def create_app(config_name):
    app = Flask(__name__, template_folder='templates')
    config_object = app_config[config_name]

    if config_object is None:
        raise Exception('No configuration found for the current environment.')

    app.secret_key = config_object.SECRET
    app.config.from_object(config_object)

    @app.route('/')
    def index():
        return 'hello world'

    return app