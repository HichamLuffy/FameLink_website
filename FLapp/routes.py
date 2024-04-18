#!/usr/bin/python3
"""quiz routes"""


from flask import render_template, url_for, flash, redirect
from FLapp import app, db
from FLapp import User, Portfolio
from FLapp import PortfolioForm

@app.route("/")
@app.route("/home")
def home():
    portfolios = Portfolio.query.all()
    return render_template('home.html', portfolios=portfolios)

@app.route("/portfolio/new", methods=['GET', 'POST'])
def new_portfolio():
    form = PortfolioForm()
    if form.validate_on_submit():
        portfolio = Portfolio(title=form.username.data, bio=form.bio.data)
        db.session.add(portfolio)
        db.session.commit()
        flash('Your portfolio has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_portfolio.html', title='New Portfolio', form=form)
