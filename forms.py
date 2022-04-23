from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, EqualTo, Email

class SignUp(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = StringField('Email', validators=[Email(), InputRequired()])
    password = PasswordField('New Password', validators=[InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')
    firstname = StringField('Firstname', validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    year = StringField('Graduation Year', validators=[InputRequired()])
    programme = StringField('Programme', validators=[InputRequired()])
    faculty = StringField('Faculty', validators=[InputRequired()])
    department = StringField('Department', validators=[InputRequired()])
    instagram = StringField('Instagram Username')
    reddit = StringField('Reddit Username')
    twitter = StringField('Twitter Username')
    submit = SubmitField('Sign Up', render_kw={'class': 'btn waves-effect waves-light white-text'})

class LogIn(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('New Password', validators=[InputRequired()])
    submit = SubmitField('Login', render_kw={'class': 'btn waves-effect waves-light white-text'})

class Edit(FlaskForm):
    username = StringField('Username')
    email = StringField('Email', validators=[Email()])
    password = PasswordField('New Password', validators=[ EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')
    firstname = StringField('Firstname')
    lastname = StringField('Lastname')
    year = StringField('Graduation Year')
    programme = StringField('Programme')
    faculty = StringField('Faculty')
    department = StringField('Department')
    instagram = StringField('Instagram Username')
    reddit = StringField('Reddit Username')
    twitter = StringField('Twitter Username')
    submit = SubmitField('Sign Up', render_kw={'class': 'btn waves-effect waves-light white-text'})