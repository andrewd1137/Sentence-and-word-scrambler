#Andrew DeMarco

import random

# dictionary for 3rd function
Int4Word = {}


# returns a random word from a sentence
def randWord(str1):
    split_string = str1.split()
    return random.choice(split_string)


# mixes words in a sentence or letters in a word (depending on length of input)
def strMixer(str1):
    split_string = str1.split()
    if len(split_string) == 1:
        shuffle_string = ''.join(random.sample(str1, len(str1)))
    else:
        shuffle_string = ' '.join(random.sample(split_string, len(split_string)))
    return shuffle_string


# assigns a random int value for a word and stores it in the dictionary
def randIntForWord(char1):
    if char1 in Int4Word.keys():
        return Int4Word[char1]

    else:
        char_int = random.randint(0, 100000)
        Int4Word.update({char1: char_int})
        return Int4Word[char1]

