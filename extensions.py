from flask_mail import Mail
from flask_wtf import CSRFProtect
from flask_login import LoginManager

mail = Mail()
csrf = CSRFProtect()
login_manager = LoginManager()
