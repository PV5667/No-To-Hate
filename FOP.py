# Full Outfile Pickle
#REQUIRES FULL OUTFILE (~250MB)
import re
import pickle

with open('outfile', 'rb') as fp:
    badlist = pickle.load(fp)

# input("What is your tweet?\n")
tweet = "TAWOHTOAHFHOAynr921yt-er 12974t19274t [oquhfd y9w7etr b9['1']]"


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


print(censor_tweet_bad_list(tweet))
