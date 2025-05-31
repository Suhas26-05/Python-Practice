# Implement a function that checks if a given string is a pangram (contains all letters of the alphabet).

import string

def is_pangram(sentence):
    alphabet_set = set(string.ascii_lowercase)
    sentence_set = set(sentence.lower())
    return alphabet_set.issubset(sentence_set)

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    if is_pangram(sentence):
        print("The sentence is a pangram.")
    else:
        print("The sentence is not a pangram.")
