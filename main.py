import re
import pickle
from itertools import product

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

with open('outfile', 'rb') as fp:
    badlist = pickle.load(fp)


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
