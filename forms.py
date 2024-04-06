#!/usr/bin/python3
"""forms Famelink app"""


import random
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from FameLink_website.models import User
from better_profanity import profanity
from flask_login import current_user
from flask import flash
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange



def validate_no_profanity(form, field):
    if profanity.contains_profanity(field.data):
        raise ValidationError('Please avoid using profane language')


class RegisterForm(FlaskForm):
    """register form"""
    username = StringField('username', validators=[DataRequired(), validate_no_profanity, Length(min=3, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = password = PasswordField('Confirm password',
                                                validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    """register form"""
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3, max=25)])
    rememberme = BooleanField('Remember me')
    submit = SubmitField('Login')
