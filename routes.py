#!/usr/bin/python3
"""quiz routes"""


import os
import secrets
import random
from PIL import Image
from werkzeug.utils import secure_filename
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from FameLink_website import app, db, bcrypt
from FameLink_website.forms import RegisterForm, LoginForm
import pymysql.cursors
from FameLink_website.models import User
from flask_login import login_user, current_user, logout_user, login_required
from flask import Blueprint, jsonify, request
from datetime import datetime
from sqlalchemy import desc
from collections import defaultdict


@app.route('/')
@app.route('/main')
def Home_page():
    return render_template('index.html', title='Home')