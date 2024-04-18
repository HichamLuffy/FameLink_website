#!/usr/bin/python3
"""forms Famelink app"""


from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, URL, Email


class PortfolioForm(FlaskForm):
    username = StringField('Title', validators=[DataRequired()])
    bio = TextAreaField('Content', validators=[DataRequired()])
    insta = StringField('Instagram', validators=[URL()])
    github = StringField('GitHub', validators=[URL()])
    twitter = StringField('Twitter', validators=[URL()])
    linkedin = StringField('LinkedIn', validators=[URL()])
    submit = SubmitField('Create Portfolio')


class ServicesSection(FlaskForm):
    service_title = StringField('Service Title', validators=[DataRequired()])
    service_description = TextAreaField('Service Description', validators=[DataRequired()])
    submit = SubmitField('Save Services')

class SkillsSection(FlaskForm):
    skill_name = StringField('Skill Name', validators=[DataRequired()])
    submit = SubmitField('Save Skills')

class MyworkSection(FlaskForm):
    pass

class EducationSection(FlaskForm):
    education_title = StringField('Education Title', validators=[DataRequired()])
    education_details = TextAreaField('Education Details', validators=[DataRequired()])
    submit = SubmitField('Save Education')

class ContactSection(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Save Contact')
