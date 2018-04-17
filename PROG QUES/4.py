"""

ID : 442

Given a string, find no.of characters to be replaced in all the words that are needed to form the word "string" by replacing the characters of that word and re-arranging them.

Finally if there such words exist print the words in lowercase and the corresponding no.of characters to be replaced else print -1.

---characters that forms the word "string" should not be replaced

Note: Punctuations are to be excluded i.e aren't can be taken as arent.

Input:

---The first line of the input contains a single integer T denoting the number of test cases.
   The description of T test cases follows.
---The first and only line of each test case consists of a string.

Output:

---print the words in lowercase and the corresponding no.of characters to be replaced.

Sample input:

1
Dictionaries aren't just for strings. Dictionary values can be any data type, including integers, booleans, arbitrary objects, or even other dictionaries. And within a single dictionary, the values don't all need to be the same type; you can mix and match as needed. Dictionary keys are more restricted, but they can be strings, integers, and a few other types. You can also mix and match key data types within a dictionary.

Sample Output:

single: 2
values: 5

Explanation:

Example case 1: Here in the given string the words single and values can be used to form the word "string" by replacing [l, e] in single with [r, t] and [v, a, l, u, e] in values with [t, r, i, n, g]

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


def main():
    """
    :return: None
    """
    for _ in range(int(stdin.readline())):
        string1 = stdin.readline().strip()
        string1 = remove_punctuations(string1)
        words = []
        for word in string1.split():
            if len(word) == 6:
                if "s" in word or "t" in word or "r" in word or "i" in word or "g" in word:
                    words.append(word.lower())
        table = {ord(char): None for char in "abcdefhjklmopquvwxyz"}
        valid = defaultdict(int)
        for word in words:
            temp = word.translate(table)
            temp = [temp.count(i) for i in temp]
            if 2 in temp:
                continue
            else:
                valid[word] = len(word)-len(word.translate(table))
        valid = sorted(valid.items())
        valid = dict(valid)
        if not valid:
            print("-1")
        else:
            for item in valid.items():
                stdout.write("{}: {}\n".format(*item))


if __name__ == "__main__":
    main()
