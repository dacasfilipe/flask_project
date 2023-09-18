import os


class Config(object):
    CSRF_ENABLED = True
    SECRET ='ysb_92=qe#djf8%ng+a*#4rt#5%3*4k5%i2bck*gn@w3@f&-&'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:root@localhost:3306/livro_flask'
    #preencha com os dados do seu banco de dados
    # user - usuário do banco
    # password - senha do usuário
    # host - geralmente no local fica localhost
    # port - padrão 3306 no mysql
    # database - nome do banco de dados


class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http://%s:%s/' %(IP_HOST,PORT_HOST)

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 5000
    URL_MAIN = 'http://%s:%s/' %(IP_HOST,PORT_HOST)

class ProductionConfig(Config):
    TESTING = False
    DEBUG = False
    IP_HOST = 'localhost'
    PORT_HOST = 8080
    URL_MAIN = 'http://%s:%s/' %(IP_HOST,PORT_HOST)

app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig(),
    'production': ProductionConfig()
}

app_active = os.getenv('FLASK_ENV', 'development')  # Default to 'development'


app_active = os.getenv('FLASK_ENV')