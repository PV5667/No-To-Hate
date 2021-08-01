###
#Dont use temp.py, instead, use main.py. It should automatically determine
#whether you need to create the full outfile
"""
import pickle
from itertools import product
# print(os.getcwd())
CHARS_MAPPING = {
    "a": ("a", "@", "*", "4"),
    "i": ("i", "*", "l", "1", "!"),
    "o": ("o", "*", "0", "@"),
    "u": ("u", "*", "v"),
    "v": ("v", "*", "u"),
    "l": ("l", "1"),
    "e": ("e", "*", "3"),
    "s": ("s", "$", "5"),
    "t": ("t", "7",),
}

with open('outfile', 'rb') as fp:
    badlist = pickle.load(fp)

def generate_leet(word):
    combos = [
        (char,
         ) if char not in CHARS_MAPPING else CHARS_MAPPING[char]
        for char in iter(word)
    ]
    return ["".join(pattern) for pattern in product(*combos)]


print("Initial badlist length " + str(len(badlist)))
for i in range(len(badlist)):
    #print(i)
    if len(badlist[i]) < 20:
        combos = [
            (char,
             ) if char not in CHARS_MAPPING else CHARS_MAPPING[char]
            for char in iter(badlist[i])
        ]
        leet = ["".join(pattern) for pattern in product(*combos)]
        for j in range(len(leet)):
            badlist.append(leet[j])
print("Final badlist length " + str(len(badlist)))
# print("Writing to outfile")

# my_file = open(my_path, 'wb')
# my_file = pickle.dump(badlist, my_file)
# print(my_file)
# my_file.close()
with open('outfile', 'wb') as fp:
    pickle.dump(badlist, fp)
"""
