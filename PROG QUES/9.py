"""
ID : 446 n 447

Given an integer, find if it is pure or not.
If pure print "YES" else print "NO".
Also print for how long the the initial blood line was pure.

A number is considered to be pure if blood groups of every ancestor of the number is same
Blood groups of ancestors of the number are the characters in the roman conversion of that number

Note: Hierarchy of ancestors is from right to left

Input:

---The first line of the input contains a single integer T denoting the number of test cases.
   The description of T test cases follows.
---The first and only line of each test case consists of an integer.

Output:

---single line containing "YES" or "NO" and also an integer denoting for how long the the initial blood line was pure.

Sample Input:

2
1000
21111

Sample Output:

YES 1
NO 1

"""

from sys import stdin, stdout
from collections import OrderedDict


def convert_to_roman(num):
    """
    :param num: An integer
    :return: A roman number
    """
    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(n):
        """
        :param n: An integer
        :return: A roman number
        """
        for r in roman.keys():
            x, y = divmod(n, r)
            yield roman[r] * x
            n -= (r * x)
            if n > 0:
                roman_num(n)
            else:
                break

    return "".join([a for a in roman_num(num)])


def main():
    """
    :return: None
    """
    for _ in range(int(stdin.readline().strip())):
        n = int(stdin.readline().strip())
        n = convert_to_roman(n)
        n = list(n)        
        if len(set(n)) == 1:
            stdout.write("YES "+str(len(n))+"\n")
        else:
            n = n[::-1]
            temp = n[0]
            count = 1
            for i in range(1, len(n)):
                if n[i] == temp:
                    count += 1
                else:
                    break
            stdout.write("NO "+str(count)+"\n")


if __name__ == "__main__":
    main()

"""

TEST CASES:

"""
