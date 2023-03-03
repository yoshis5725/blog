import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy  # installed flask_sqlalchemy module
from flask_migrate import Migrate  # installed flask_migrate
from blog.core.views import core
from blog.errorPages.handlers import error_pages


app = Flask(__name__)


# ----- Database Configuration -----

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


# ----- Login Configurations -----
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'


# ----- Blueprint Registrations -----

app.register_blueprint(core)
app.register_blueprint(error_pages)
