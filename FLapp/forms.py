#!/usr/bin/python3
"""forms Famelink app"""


from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class PortfolioForm(FlaskForm):
    username = StringField('Title', validators=[DataRequired()])
    bio = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Create Portfolio')