# config.py

class Config(object):
    """
    Common configuration
    """
    DEBUG = True

class DevelopmentConfig(Config):
    """
    Development configuration
    """

    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

class TestingConfig(Config):
    """
    Testing configuration
    """

    TESTING = True

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}



# Enable Flask's Debugging features.Should be False in production

