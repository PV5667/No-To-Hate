import re
from profanity_check import predict, predict_prob
import pickle
# from better_profanity import Profanity
from itertools import product

with open('outfile', 'rb') as fp:
    badlist = pickle.load(fp)
print("Final badlist length " + str(len(badlist))) # should that be 13061640
print(str(len(badlist))==13061640)
tweet = input("What is your tweet?\n")


def censor_tweet(tweet):
    originaltweet = tweet.split()
    tweet = re.sub(r'[^\w\s]', '', tweet)
    tweet_list = tweet.lower().split()
    for i in range(len(tweet_list)):
        tweet_array = [tweet_list[i]]
        if predict(tweet_array) == 1:
            originaltweet[i] = '*' * len(originaltweet[i])
    censor_string = ' '.join(originaltweet)
    return censor_string


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


print(censor_tweet(tweet))
print(censor_tweet_bad_list(tweet))
