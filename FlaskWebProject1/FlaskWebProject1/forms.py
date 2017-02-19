from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, IntegerField, PasswordField
from wtforms.validators import Required
from wtforms.validators import Length, Email

class SignUp(FlaskForm):
    username = TextField('Choose your username', validators=[Required()])
    email = TextField('Email address', validators=[
           Required('Please provide a valid email address'),
           Length(min=6, message=(u'Email address too short')),
           Email(message=(u'That\'s not a valid email address.'))])
    password = PasswordField('Password', validators=[
           Required(),
           Length(min=3, message=(u'Please give a longer password'))])

class LogIn(FlaskForm):
     password = PasswordField('Password', validators=[
           Required(),
           Length(min=3, message=(u'Please give a longer password'))])
     username = TextField('Username', validators=[Required()])