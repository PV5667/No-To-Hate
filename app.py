from flask import Flask, flash, jsonify, render_template, request
from flask.templating import render_template
import re
from profanity_check import predict, predict_prob
import pickle
import tensorflow as tf
import numpy as np


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

def run_through_model(tweet):

    model = tf.keras.models.load_model('weights1.h5')
    prediction = model.predict(np.array([tweet]))
    for i in prediction:
        labels = ['hate', 'normal']
        return labels[np.argmax(i)]


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
    model_prediction = run_through_model(tweet)
    return render_template("handling.html", user_name=user_name, censored_string=censored_string, model_prediction = model_prediction)

if __name__ == "__main__":
    app.run(debug=True)






