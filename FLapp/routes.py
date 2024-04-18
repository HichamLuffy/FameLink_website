#!/usr/bin/python3
"""quiz routes"""


from flask import render_template, url_for, flash, redirect
from FLapp import app, db
from FLapp import User, Portfolio
from FLapp import PortfolioForm, SkillsSection, MyworkSection, EducationSection, ContactSection, ServicesSection


@app.route("/")
@app.route("/home")
def home():
    portfolios = Portfolio.query.all()
    return render_template('index.html', portfolios=portfolios)

@app.route("/portfolio/new", methods=['GET', 'POST'])
def new_portfolio():
    form = PortfolioForm()
    service = ServicesSection()
    skills = SkillsSection()
    mywork = MyworkSection()
    education = EducationSection()
    contact = ContactSection()
    if form.validate_on_submit():
        form_data = form.data
        service = service.data
        skills = skills.data
        mywork = mywork.data
        education = education.data
        contact = contact.data
        # Pass the form data to the next HTML template
        return render_template('newportfolio.html', form_data = form_data, contact = contact, service = service,
                                skills = skills, mywork = mywork, education = education)
    
    return redirect('/home')