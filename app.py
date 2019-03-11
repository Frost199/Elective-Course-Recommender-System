from flask import Flask
# Blueprints Imports
from blueprints.page import page
from blueprints.users import user
from blueprints.questions import aos_test, elective_course

# extensions Import
from extensions import mail, csrf, login_manager

CELERY_TASK_LIST = ['blueprints.contact.tasks', ]

# app = Flask(__name__, instance_relative_config=True)
# app.config.from_object('config.settings')
# app.config.from_pyfile('settings.py', silent=True)
#
# app.register_blueprint(page)


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    application = Flask(__name__, instance_relative_config=True)

    application.config.from_object('config.settings')
    application.config.from_pyfile('settings.py', silent=True)

    if settings_override:
        application.config.update(settings_override)

    application.register_blueprint(page)
    application.register_blueprint(user)
    application.register_blueprint(aos_test)
    application.register_blueprint(elective_course)
    extensions(application)

    return application


def extensions(our_app):

    mail.init_app(our_app)
    csrf.init_app(our_app)
    login_manager.init_app(our_app)
    login_manager.login_view = 'user.login'
    login_manager.login_message_category = 'info'
    return None
