from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello ip"

@app.route("/About")
def about():
    return "About this"


if __name__ == "__main__":
    app.run(debug=True)