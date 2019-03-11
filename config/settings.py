import secrets

DEBUG = True

SERVER_NAME = "127.0.0.1:5990"
SECRET_KEY = secrets.token_hex(32)

SQLALCHEMY_DATABASE_URI = 'sqlite:///database/data.db'

# Flask-Mail
MAIL_DEFAULT_SENDER = "contact@local.host"
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = "you@gmailcom"
MAIL_PASSWORD = "yourpassword"

# Celery
CELERY_BROKER_URL = 'redis://:devpassword@redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://:devpassword@redis:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5
