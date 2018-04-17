"""
ID : 440

Given a string, print the word counts of valid words in the string in a sorted manner.

Here a word is considered to be valid if k%n=0 where
---k is the sum of ascii values of individual characters of a word.
---n is the length of the word.

Note: Punctuations are to be excluded i.e aren't can be taken as arent.

Input:

---The first and only line of the input consists of a string.

Output:

---Print the word counts of valid words in the string.

Sample Input:

Dictionaries aren't just for strings. Dictionary values can be any datatype, including integers, booleans, arbitrary objects, or even other dictionaries. And within a single dictionary, the values don't all need to be the same type; you can mix and match as needed. Dictionary keys are more restricted, but they can be strings, integers, and a few other types. You can also mix and match key datatypes within a dictionary.

Sample Output:

a: 3
are: 1
as: 1
can: 4
for: 1
keys: 1
match: 2
need: 1
single: 1
the: 2
types: 1

Explanation :

Value of k for a is 97 and is divisible by its length so its a valid word.

"""

import string
from collections import defaultdict
from sys import stdin, stdout


def remove_punctuations(sentence):
    """
    :param sentence: A string.
    :return: A string with punctuations removed.
    """
    table = string.punctuation
    table = {ord(char): None for char in table}
    return sentence.translate(table)


def valid_words(sentence):
    """
    :param sentence: string returned by the remove_punctuations() function
    :return: valid words as per the problem statement
    """
    sums = []
    for word in sentence:
        temp = [ord(i) for i in word]
        sums.append(sum(temp)%len(word))
    return " ".join(sentence[i] for i in range(len(sentence)) if sums[i] == 0)


def main():
    """
    :return: None
    """
    sentence = stdin.readline().strip()
    sentence = remove_punctuations(sentence)
    sentence = sentence.split()
    sentence = valid_words(sentence)
    words = defaultdict(int)
    for word in sentence.split():
        words[word] += 1
    words = sorted(words.items())
    words = dict(words)
    for item in words.items():
        stdout.write("{}: {}\n".format(*item))


if __name__ == "__main__":
    main()
