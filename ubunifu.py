from flask import Flask,render_template,url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config["SECRET_KEY"] = '450922fba6e46eeb36b12d8a7635aa92836d3dbe'
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

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form = form)  #title="login"



if __name__ == "__main__":
    app.run(debug=True)