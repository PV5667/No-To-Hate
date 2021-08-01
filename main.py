import re
import pickle

with open('badlist', 'rb') as fp:
    badlist = pickle.load(fp)

def censor(tweet):
    originaltweet = tweet.split()
    tweet_list = tweet.lower().split()
    for i in range(len(tweet_list)):
        try:
            temp = badlist.index(tweet_list[i])
            originaltweet[i] = '*' * len(originaltweet[i])
        except:
            pass
    censor_string = ' '.join(originaltweet)
    return censor_string
