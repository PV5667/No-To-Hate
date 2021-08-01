# Minimal Outfile json
import re
import json
from itertools import product
import timeit

CHARS_MAPPING = {
    "a": ("a", "*", "@"),
    "i": ("i", "*", "l", "1", "!"),
    "o": ("o", "*", "0",),
    "u": ("u", "*", "v"),
    "v": ("v", "*", "u"),
    "l": ("1"),
    "h": ("#"),
    "e": ("e", "*"),
    "s": ("s", "$"),
    "t": ("t", "7", "%"),
}
num = 10000


def file():
    with open('data - Copy.json', 'r') as f:
        badlist = json.load(f)


openfileT = timeit.Timer(file).timeit(number=num) / num

for i in range(len(badlist)):
    if len(badlist[i]) < 20:
        combos = [
            (char,
             ) if char not in CHARS_MAPPING else CHARS_MAPPING[char]
            for char in iter(badlist[i])
        ]
        leet = ["".join(pattern) for pattern in product(*combos)]
        for j in range(len(leet)):
            badlist.append(leet[j])

# input("What is your tweet?\n")
tweet = "TAWOHTOAHFHOAynr921yt-er 12974t19274t [oquhfd y9w7etr b9['1']]"


def censor(tweet):
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
