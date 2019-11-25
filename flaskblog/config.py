import os
class Configuration(object):
    DEBUG = True;
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/mydb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'c37d16ecaa048eb2d98147b54ea28321'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'nurlantukenbayev@gmail.com'
    MAIL_PASSWORD = 'scottparker2525'
