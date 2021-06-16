from datetime import datetime
from flask import Flask,render_template,url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config["SECRET_KEY"] = '450922fba6e46eeb36b12d8a7635aa92836d3dbe'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpeg")
    password = db.Column(db.String(20), nullable=False)
    posts = db.relationship('Post',backref='author', lazy=True)
    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100),nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)


    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"




@app.route("/")
def index():
    title = "Ubunifu;the creatives haven"
    return render_template("index.html",title=title)
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('index'))
    return render_template("register.html", form = form) #title="Register"
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "jj@gmail.com" and form.password.data =="password":
            flash('You have been logged in', 'success')
            return redirect(url_for('index'))
    else:
        flash('Login unsucessful.Please check username and password')
    return render_template("login.html", form = form)  #title="login"
if __name__ == "__main__":
    app.run(debug=True)