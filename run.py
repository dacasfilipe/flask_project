from app import create_app
from config import app_config, app_active

config_object = app_config[app_active]
app_instance = create_app(app_active)

if __name__ == '__main__':
    app_instance.run(host=config_object.IP_HOST, port=config_object.PORT_HOST)

#export	FLASK_ENV=development