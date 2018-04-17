"""
ID : 445

Given an array of strings, print all the fibonacci words.

A word is said to be a fibonacci word if k%fibonacci(a,b) = 0 where
a is the value of the starting character of the word.
b is the value of the ending character of the word.
k is the length of the word.

If there are no fibonacci words in the array print -1

Note: value means alphabetical values a-z or A-Z(1-26)

Input:

---The first line of the input contains a single integer T denoting the number of test cases.
   The description of T test cases follows.
---The first and only line of each test case consists of an array of strings.

Output:

---Single line containing space separated fibonacci words.

Sample Input:

1
arc architecture bag boing biotic

Sample Output:

biotic

Explanation:

Example case 1: fibonacci numbers in between b and c of biotic (2,3)
                length of biotic is 6, 6%2 is 0 and 6%3 is 0
"""

from sys import stdin, stdout


def fun():
    """
    :return: Integer
    """
    initial_1, initial_2 = 0, 1
    while True:
        yield initial_1
        initial_1, initial_2 = initial_2, initial_1 + initial_2


def fib(start, end):
    """
    :param start: Integer value of the starting character of the word.
    :param end: Integer value of the ending character of the word.
    :return: Integer
    """
    for cur in fun():
        if cur > end:
            return
        if cur >= start:
            yield cur


def main():
    """
    :return: None
    """
    for _ in range(int(stdin.readline().strip())):
        arr = stdin.readline().strip().split()
        words = []
        for i in arr:
            i = i.lower()
            count = 0
            flag = 0
            for j in fib(ord(i[0])-96, ord(i[len(i)-1])-96+1):
                flag += 1
                try:
                    if len(i) % j == 0:
                        count += 1
                except ZeroDivisionError:
                    break
            if (count != 0 and flag != 0) and count == flag:
                words.append(i)
        if words:
            for word in words:
                stdout.write(word+" ")
        else:
            print("-1")

if __name__ == "__main__":
    main()
