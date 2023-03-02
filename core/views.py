from flask import redirect, render_template, request, Blueprint


core = Blueprint('core', __name__)


# ----- Views -----

@core.route('/')
def index():
    return render_template('index.html')


@core.route('/info')
def info():
    return render_template('info.html')




