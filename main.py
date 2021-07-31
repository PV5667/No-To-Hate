import re
from profanity_check import predict, predict_prob

tweet = input("What is your tweet?\n")


def censor_tweet(tweet):
    tweet = re.sub(r'[^\w\s]', '', tweet)
    tweet_list = tweet.lower().split()
    for i in range(len(tweet_list)):
        print("running")
        tweet_array = [tweet_list[i]]
        if predict(tweet_array) == 1:
            tweet_list[i] = '*' * len(tweet_list[i])
    censor_string = ' '.join(tweet_list)
    return censor_string


print(censor_tweet(tweet))
