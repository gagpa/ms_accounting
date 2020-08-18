import os


class Config:
    MONGODB_SETTINGS = {
        'db': os.environ.get('DB'),
        'host': os.environ.get('DB_HOST'),
        'port': os.environ.get('DB_PORT'),
        'username': os.environ.get('DB_USERNAME'),
        'password': os.environ.get('DB_PASSWORD'),
    }


    def init_app(self, app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


main_config = {'default': DevelopmentConfig,
               'development': DevelopmentConfig,
               'production': ProductionConfig,
               }
