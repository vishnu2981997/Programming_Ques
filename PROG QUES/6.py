"""

ID : 444

Given an integer array, check if it is a subset of prime factors of N
where N is the least common multiple of whole numbers from 1 to 100.

Print "YES" if the array is a subset of prime factors of N else print "NO".

Input:

---The first line of the input contains a single integer T denoting the number of test cases.
   The description of T test cases follows.
---First line of each test case consists of an integer n representing no.of elements in the array.
---Next line consists of a space separated array of integers.

Output:

---YES or NO for each test cases.

Sample input:

2
3
13 7 11
10
61 15 32 96 53 74 11 94 93 3

Sample Output:

YES
NO

"""

from sys import stdin, stdout


def subset(arr2, arr1, size_arr2, size_arr1):
    """
    :param arr1: Prime factors of N.
    :param arr2: User input array.
    :param size_arr1: Length of arr1.
    :param size_arr2: Length of arr2.
    :return: Either 1 or 0.
    """
    i = 0
    j = 0
    for i in range(size_arr1):
        for j in range(size_arr2):
            if arr1[i] == arr2[j]:
                break
        if j == size_arr2-1:
            return 0
    return 1


def primes_nums(arr_size):
    """
    :param n: 100 as per the program statement.
    :return: Prime numbers.
    """
    primes = [True for i in range(arr_size + 1)]
    prime = 2
    arr = []
    while prime * prime <= arr_size:
        if primes[prime]:
            for i in range(prime * 2, arr_size + 1, prime):
                primes[i] = False
        prime += 1
    for num in range(2, arr_size):
        if primes[num]:
            arr.append(num)
    return arr


def main():
    """
    :return: None
    """
    for _ in range(int(stdin.readline().strip())):
        arr_size = int(stdin.readline().strip())
        arr1 = [int(i) for i in stdin.readline().strip().split()]
        arr2 = primes_nums(100)
        for i in arr2:
            if i*i > 100:
                break
            else:
                for j in range(2, 8):
                    if i**j > 100:
                        arr2.append(i**(j-1))
                        break
        arr2 = sorted(arr2)
        print(*arr2)
        if subset(arr2, arr1, len(arr2), arr_size):
            stdout.write("YES\n")
        else:
            stdout.write("NO\n")


if __name__ == "__main__":
    main()
