import re
from profanity_check import predict, predict_prob
import pickle
# from better_profanity import Profanity
from itertools import product

with open('outfile', 'rb') as fp:
    badlist = pickle.load(fp)

tweet = 'handjob'  # input("What is your tweet?\n")


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


def generate_leet(word):
    CHARS_MAPPING = {
        "a": ("a", "@", "*", "4"),
        "i": ("i", "*", "l", "1"),
        "o": ("o", "*", "0", "@"),
        "u": ("u", "*", "v"),
        "v": ("v", "*", "u"),
        "l": ("l", "1"),
        "e": ("e", "*", "3"),
        "s": ("s", "$", "5"),
        "t": ("t", "7",),
    }
    combos = [
        (char,
         ) if char not in CHARS_MAPPING else CHARS_MAPPING[char]
        for char in iter(word)
    ]
    return ["".join(pattern) for pattern in product(*combos)]


def censor_tweet_leet(tweet):
    return Profanity.censor(tweet)

print(generate_leet("test"))
# print(censor_tweet(tweet))
# print(censor_tweet_bad_list(tweet))
# print(censor_tweet_leet(tweet))
