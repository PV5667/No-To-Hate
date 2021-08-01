import pickle
from itertools import product

CHARS_MAPPING = {
    "a": ("a", "*", "@"),
    "i": ("i", "*", "l", "1", "!"),
    "o": ("o", "*", "0",),
    "u": ("u", "*", "v"),
    "v": ("v", "*", "u"),
    "l": ("l", "1"),
    "h": ("h", "#"),
    "e": ("e", "*"),
    "s": ("s", "$"),
    "t": ("t", "7", "%"),
}

with open('outfile', 'rb') as fp:
    badlist = pickle.load(fp)
#
for i in range(len(badlist)):
    if len(badlist[i]) < 20:
        combos = [
            (char,
             ) if char not in CHARS_MAPPING else CHARS_MAPPING[char]
            for char in iter(badlist[i])
        ]
        leet = ["".join(pattern) for pattern in product(*combos)]
        if(badlist[i] == 'shit'):
            print(leet)
        badlist.extend(leet)
print(len(badlist))
with open('badlist', 'wb') as fp:
    pickle.dump(badlist, fp)
badlist.index("$hit")

# def permute(word):
#     combos = [
#         (char,
#          ) if char not in CHARS_MAPPING else CHARS_MAPPING[char]
#         for char in iter(word)
#     ]
#     leet = ["".join(pattern) for pattern in product(*combos)]
#     return leet
# list = permute("shit")
# print(list.index("$hit"))

# def censor(tweet):
#     originaltweet = tweet.split()
#     tweet_list = tweet.lower().split()
#     for i in range(len(tweet_list)):
#         try:
#             temp = badlist.index(tweet_list[i])
#             originaltweet[i] = '*' * len(originaltweet[i])
#         except:
#             pass
#     censor_string = ' '.join(originaltweet)
#     return censor_string
# print(censor("$hit"))
