from flask_app.models.model_user import User

from flask_app import app
from flask import render_template, redirect, flash, session, request
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def main():
    return redirect('/main')

@app.route('/main')
def index():

    return render_template('main.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/signup')
def signup():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():

    #validates information input, redirects to same page if incorrect
    valid = User.validate_info(request.form)
    if not valid: 
        return redirect('/signup')
    
    #processes the information below if it is valid! 
    #hash the password and set it apart of the data being passed in. 
    data = {
        'first' : request.form['first'],
        'last' : request.form['last'],
        'email' : request.form['email'],
        'pw_hash' : bcrypt.generate_password_hash(request.form['password'])
    }
    user = User.create_user(data)

    #declare the session/logs in user
    session['user_id'] = user
    print("SESSION INFO: ",session['user_id'])
    
    return redirect('/ideas')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login-user', methods=['POST'])
def login_user():
        # get user by the email
    user = User.get_user_by_email(request.form)
    if not user:
        flash('Invalid Email or Password', 'login')
        return redirect('/login')
    
    # check hashed password against the inputted password
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Invalid Email or Password', 'login')
        return redirect('/login')

    # if everything passes, log in the user 
    session['user_id'] = user.id 
    print("SESSION INFO: ",session['user_id'])
    return redirect('/ideas')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/main')