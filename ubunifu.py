from flask import Flask,render_template

app = Flask(__name__)

app.config["SECRET_KEY"] = '450922fba6e46eeb36b12d8a7635aa92836d3dbe'

@app.route("/")
def index():
    title = "Ubunifu;the creatives haven"
    return render_template("index.html",title=title)


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("about.html")

