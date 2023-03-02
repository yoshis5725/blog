from flask import Flask
from blog.core.views import core
from blog.errorPages.handlers import error_pages


app = Flask(__name__)


# ----- Blueprint Registrations -----

app.register_blueprint(core)
app.register_blueprint(error_pages)
