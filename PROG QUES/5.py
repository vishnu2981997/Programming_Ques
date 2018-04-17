"""
ID : 443

Given a set of strings and a condition, check if they are valid or not based on given condition.
Condition string is made using uppercase letters, uppercase letter, lowercase letters, lowercase letter, numbers, number
separated by commas.

eg: numbers, uppercase letters, numbers

Note: Strings are not case sensitive

Input:

---The first line of the input contains a single integer T denoting the number of test cases.
   The description of T test cases follows.
---The first line of each test case consists of the condition as specified in the problem.
---The second line consists of a single integer n denoting number of strings.
---The following n lines consists of the strings.

Output:

---Yes or No for each string for all test cases.

Sample Input:

2
numbers, uppercase letters, numbers
3
1B2
10L1
1N200J1
numbers, uppercase letters, numbers
3
11B
10LAAAAAAA1
1AA20J1

Sample Output:

Yes
Yes
Yes
No
Yes
Yes

Explanation:

Example case 1: 1B2 numbers followed by uppercase letters followed by numbers [1,B,2]
                10L1 numbers followed by uppercase letters followed by numbers [10,L,1]
                1N200J1 numbers followed by uppercase letters followed by numbers [1,N,200,J,1]

Example case 2: 11B numbers followed by uppercase letters [11,B]
                Here uppercase letters are not being followed by numbers so No

"""

import re
from sys import stdin


def make_regex(string):
    """
    :param string: Array of strings.
    :return: A string
    """
    pattern = """p = re.compile("^("""
    for i in string:
        if i == "uppercase letter":
            pattern += "[A-Z]"
        elif i == "lowercase letter":
            pattern += "[a-z]"
        elif i == "number":
            pattern += "[0-9]"
        elif i == "uppercase letters":
            pattern += "[A-Z]+"
        elif i == "lowercase letters":
            pattern += "[a-z]+"
        elif i == "numbers":
            pattern += "[0-9]+"
        else:
            continue
    pattern += """)+$")"""
    return pattern


def main():
    """
    :return: None
    """
    for _ in range(int(stdin.readline().strip())):
        string = stdin.readline().strip()
        string = string.split(", ")
        string = [i.lower() for i in string]
        pattern = make_regex(string)
        exec(pattern)
        n = int(stdin.readline().strip())
        strings = []
        for i in range(n):
            strings.append(stdin.readline().strip())
        for i in strings:
            m = """print("Yes" if p.match(i) else "No")"""
            exec(m)


if __name__ == "__main__":
    main()
