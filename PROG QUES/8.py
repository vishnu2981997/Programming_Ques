"""

Given a word and a number, from all possibilities of the word
print the values of the words greater than the given number.
If there are no values print -1.

Note: All characters in the word should be in lowercase

Input:

---The first line of the input contains a single integer T denoting the number of test cases.
   The description of T test cases follows.
---The first and only line of each test case consists of a word and a number separated by space.

Output:

--- A space separated array of integers.

Sample Input:

1
abc 200

Sample Output:

213 231 312 321

"""

import itertools
from sys import stdin, stdout


def main():
    """
    :return: None
    """
    for _ in range(int(stdin.readline().strip())):
        word, num = [i for i in stdin.readline().strip().split()]
        p = itertools.permutations(word, len(word))
        arr = []
        for i in p:
            number = ""
            for j in i:
                j = j.lower()
                number = number + str(ord(j)-96)
            arr.append(int(number))
        arr = set(sorted(arr))
        arr = [i for i in arr if i >= int(num)]
        arr = sorted(arr)
        if arr:
            for i in arr:
                stdout.write(str(i)+" ")
            stdout.write("\n")
        else:
            stdout.write("-1\n")


if __name__ == "__main__":
    main()
