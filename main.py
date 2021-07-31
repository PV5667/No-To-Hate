import re
from profanity_check import predict, predict_prob

tweet = input("What is your tweet?\n")


def censor_tweet(tweet):
    originaltweet = tweet.split()
    tweet = re.sub(r'[^\w\s]', '', tweet)
    tweet_list = tweet.lower().split()
    for i in range(len(tweet_list)):
        print("In for loop")
        tweet_array = [tweet_list[i]]
        if predict(tweet_array) == 1:
            originaltweet[i] = '*' * len(originaltweet[i])
    censor_string = ' '.join(originaltweet)
    return censor_string


print(censor_tweet(tweet))
