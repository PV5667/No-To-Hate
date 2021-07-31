from flask import Flask, flash, jsonify, render_template, request
from flask.templating import render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/black-list")
def black_list():
    return render_template("BlackList.html")

@app.route("/real-world")
def real_world():
    return render_template("RealWorld.html")

@app.route("/handling", methods=['POST'])
def handling():
    tweet = request.form['tweet']
    user_name = request.form['user_name']
    return f"<h1>Hi {user_name}, your tweet was: {tweet} <h1>"

if __name__ == "__main__":
    app.run(debug=True)

