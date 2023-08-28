from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import BooleanField, StringField, PasswordField, Form
from wtforms import validators


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])


class FileApiForm(Form):
    file = FileField('file', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])


class FileForm(FlaskForm):
    file = FileField('file', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
