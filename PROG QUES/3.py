"""

ID : 441

Given a path, verify if it is a path or not.
print VALID if valid else NOT VALID if not.

Note: all paths starts from "\".

Input:

---The first line of the input contains a single integer T denoting the number of test cases.
   The description of T test cases follows.
---The first and only line of each test case consists of a string.

Output:

---Single line containing VALID or NOT VALID

Sample Input:

2
\a\b
\s\f\g

Sample Output:

VALID
VALID

"""

from sys import stdin, stdout


def main():
    """
    :return: None
    """
    for _ in range(int(stdin.readline().strip())):
        path = stdin.readline().strip()
        path = path.replace("\\", " \\ ")
        if "/" in path:
            stdout.write("NOT VALID")
        else:
            path = path.split()
            path = [path[i] for i in range(0, len(path), 2)]
            if ((len(set(path)) == 1) and (set(path) == {"\\"})):
                stdout.write("VALID\n")
            else:
                stdout.write("NOT VALID\n")


if __name__ == "__main__":
    main()
