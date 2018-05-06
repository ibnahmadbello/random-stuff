# This program will receive a scramble word and bring out all possible arrangement of the word.
# I used permutation to get the number of possible arrangement

import random

def main():
    scrambled_word = input("Enter the scrambled word here:\n")
    scrambled_length = len(scrambled_word)
    original_word = ""


# for letters in scrambled_word:
def trial(word, new):
    for letters in word:
        position = random.randrange(len(word))
        new += word[position]
        word = word[:position] + word[(position + 1):]
        if len(new) == scrambled_length:
            print(new, end="\t")


for i in range(numberOfPossiblePermutation(scrambled_length)):
    trial(scrambled_word, original_word)
input("\nPress Enter key to exit.")


def numberOfPossiblePermutation(scrambled_length):
    result = 1
    while scrambled_length > 1:
        result *= scrambled_length
        --scrambled_length
    return result