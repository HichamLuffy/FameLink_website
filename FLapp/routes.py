#!/usr/bin/python3
"""FLapp"""


from flask import render_template, url_for, flash, redirect
from FLapp import app, db
from FLapp.forms import PortfolioForm, SkillsSection, MyworkSection, EducationSection, ContactSection, ServicesSection


@app.route("/")
@app.route("/home")
def home():
    form = PortfolioForm()
    service = ServicesSection()
    skills = SkillsSection()
    mywork = MyworkSection()
    education = EducationSection()
    contact = ContactSection()
    return render_template('index.html', title="portfolios", form=form, contact = contact, service = service,
                                skills = skills, mywork = mywork, education = education)

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