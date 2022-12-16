from flask_app.models.model_user import User

from flask_app import app
from flask import render_template, redirect, flash, session, request

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')
    