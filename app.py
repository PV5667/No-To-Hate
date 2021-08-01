from flask import Flask, flash, jsonify, render_template, request
from flask.templating import render_template
import re
from profanity_check import predict, predict_prob
import pickle

app = Flask(__name__)

with open('outfile', 'rb') as fp:
    badlist = pickle.load(fp)


def censor_tweet_bad_list(tweet):
    originaltweet = tweet.split()
    tweet = re.sub(r'[^\w\s]', '', tweet)
    tweet_list = tweet.lower().split()
    for i in range(len(tweet_list)):
        try:
            temp = badlist.index(tweet_list[i])
            originaltweet[i] = '*' * len(originaltweet[i])
        except:
            pass
    censor_string = ' '.join(originaltweet)
    return censor_string

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
    censored_string = censor_tweet_bad_list(tweet)
    return f"<h1>Hi {user_name}, your censored tweet is: {censored_string} <h1>"

if __name__ == "__main__":
    app.run(debug=True)






