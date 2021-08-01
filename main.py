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

def permute(word)
    combos = [
        (char,
         ) if char not in CHARS_MAPPING else CHARS_MAPPING[char]
        for char in iter(word)
    ]
    leet = ["".join(pattern) for pattern in product(*combos)]

print(permute("shit"))
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
