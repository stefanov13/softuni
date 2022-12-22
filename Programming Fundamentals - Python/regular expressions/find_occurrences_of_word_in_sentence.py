import re

def word_counts(wanted_word, given_string):
    return len(re.findall(fr"\b{wanted_word}\b", given_string, re.IGNORECASE))


text = input()
key_word = input()

print(word_counts(key_word, text))
