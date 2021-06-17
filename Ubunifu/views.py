import secrets
import os
from flask import render_template,url_for, flash, redirect, request, abort
from ubunifu import app, db ,bcrypt
from ubunifu.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from ubunifu.models import User,Post 
from flask_login import login_user,current_user,login_required,logout_user



@app.route("/")
@app.route("/home")
def index():
    # title = "Ubunifu;the creatives haven"
    posts = Post.query.all()
    return render_template('index.html', posts=posts )     #title='title'


# ----------------------------REGISTER ROUTE-------------------------

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account has been  created,you can log in.', 'success')
        return redirect(url_for('login'))
    return render_template("register.html",title="Register", form = form) 


# --------------------------LOG IN ROUTE-------------------------------

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email =form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login unsucessful.Please check username and password', 'danger')
    return render_template("login.html",title="Login", form = form)  





