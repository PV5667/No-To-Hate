<<<<<<< HEAD
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


# print(censor_tweet(tweet))
=======
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
>>>>>>> 41e20644349b5cda2b951e9715b589f0f565d920
