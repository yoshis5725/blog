from flask import render_template, url_for, flash, request, redirect, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from blog import db
from blog.models import User, BlogPost
from blog.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from blog.users.picture_handler import add_profile_pic


users = Blueprint('users', __name__)


# ----- Views -----

@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        # creating the user
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)

        # ----- saving the user to the database -----
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # querying the user
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Log in Successful')

            next_page = request.args.get('next')

            if next_page is None or not next[0] == '/':
                next_page = url_for('core.index')

            return redirect(next_page)

    return render_template('login.html', form=form)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index'))




