#Andrew DeMarco

import random

Int4Word = {}


def randWord(str1):
    split_string = str1.split()
    return random.choice(split_string)


def strMixer(str1):
    split_string = str1.split()
    if len(split_string) == 1:
        shuffle_string = ''.join(random.sample(str1, len(str1)))
    else:
        shuffle_string = ' '.join(random.sample(split_string, len(split_string)))
    return shuffle_string


def randIntForWord(char1):
    if char1 in Int4Word.keys():
        return Int4Word[char1]

    else:
        char_int = random.randint(0, 100000)
        Int4Word.update({char1: char_int})
        return Int4Word[char1]

