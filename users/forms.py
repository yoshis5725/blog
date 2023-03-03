from flask_wtf import FlaskForm  # imported the library
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed  # allows the update of png or jpeg file
from flask_login import current_user
from blog.models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired, Email()])
    password = PasswordField('Password', validators=[DataRequired()])  # will be saving the hash version
    submit = SubmitField('Log in')


class Registration(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired, Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(), EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

    # ----- Verifications -----

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This email has been registered already')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This username has been registered already')


class UpdateUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired, Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    # ----- Verifications -----

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This email has been registered already')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This username has been registered already')


