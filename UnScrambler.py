# This program will receive a scramble word and bring out all possible arrangement of the word.
# I used permutation to get the number of possible arrangement

import random

scrambled_word = input("Enter the scrambled word here:\n")
scrambled_length = len(scrambled_word)
original_word = ""

def main():
    print(getWordFactorial(scrambled_length))
    for i in range(getWordFactorial(scrambled_length)):
        word = getRandomWord()
        if word.upper() in ENGLISH_WORDS:
            print(word)


# # for letters in scrambled_word:
# def trial(word, new):
#     for letters in word:
#         position = random.randrange(len(word))
#         new += word[position]
#         word = word[:position] + word[(position + 1):]
#         if len(new) == scrambled_length:
#             print(new, end="\t")
#
#
# for i in range():
#     trial(scrambled_word, original_word)
# input("\nPress Enter key to exit.")
#
#
# def numberOfPossiblePermutation(scrambled_length):
#     result = 1
#     while scrambled_length > 1:
#         result *= scrambled_length
#         --scrambled_length
#     return result


def getWordFactorial(scrambled_length):
    result = 1
    while scrambled_length > 1:
        result = result * scrambled_length
        scrambled_length = scrambled_length - 1
    return result

def getRandomWord():
    newWord = list(scrambled_word)
    random.shuffle(newWord)
    return ''.join(newWord)

def loadDictionary():
    dictionaryFile = open('dictionary.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords

ENGLISH_WORDS = loadDictionary()

if __name__ == '__main__':
    main()