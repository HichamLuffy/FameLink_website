#!/usr/bin/python3
"""forms Famelink app"""


from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, URL, Email, Optional


class PortfolioForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    bio = TextAreaField('Bio', validators=[DataRequired()])
    insta = StringField('Instagram', validators=[Optional(), URL(require_tld=False)])
    github = StringField('GitHub', validators=[Optional(), URL(require_tld=False)])
    twitter = StringField('Twitter', validators=[Optional(), URL(require_tld=False)])
    linkedin = StringField('LinkedIn', validators=[Optional(), URL(require_tld=False)])
    submit = SubmitField('Create Portfolio')



class ServicesSection(FlaskForm):
    service_title = StringField('Service Title', validators=[DataRequired()])
    service_description = TextAreaField('Service Description', validators=[DataRequired()])
    submit = SubmitField('Save Services')

class SkillsSection(FlaskForm):
    skill_name = StringField('Skill Name', validators=[DataRequired()])
    submit = SubmitField('Save Skills')

class MyworkSection(FlaskForm):
    work_title = StringField('Work Title', validators=[DataRequired()])
    work_description = TextAreaField('Work Description', validators=[DataRequired()])
    work_link = StringField('Work URL', validators=[Optional(), URL(require_tld=False)])
    submit = SubmitField('Save Work')

class EducationSection(FlaskForm):
    education_title = StringField('Education Title', validators=[DataRequired()])
    education_details = TextAreaField('Education Details', validators=[DataRequired()])
    submit = SubmitField('Save Education')

class ContactSection(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Save Contact')
