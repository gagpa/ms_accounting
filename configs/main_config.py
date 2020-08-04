class Config:

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
