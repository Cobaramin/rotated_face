class Config:
    DEBUG = False
    PORT = 80
    HOST = '0.0.0.0'


class Development(Config):
    DEBUG = True

class Production(Config):
    DEBUG = False
