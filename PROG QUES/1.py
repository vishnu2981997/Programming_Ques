"""
ID: 437

Given an array of n numbers. sort the array in ascending order based on given conditions:

---convert the elements of array to filesize formats
---convert the file sizes to corresponding binary representations
---sort the actual array based on number of 1's present in the binary representation of their
   file sizes.

Note: File sizes should be in integer format
      Consider file size till YB (B, KB, MB, GB, TB, PB, EB, ZB, YB)

Input:

---The first line of the input contains a single integer T denoting the number of test cases.
   The description of T test cases follows.
---First line of each test case consists of a single integer n denoting the size of the
   array.
---The second line of each test case contains n space separated integers.

Output:

---For each test case, print a single line containing the sorted array.

Sample Input:

3
10
1 2 3 4 5 6 7 8 9 10
10
1024 1025 1026 1027 1028 1029 1030 1031 1032 1033
3
2048 1024 3072

Sample Output:

1 2 4 8 3 5 6 9 10 7
1024 1025 1026 1027 1028 1029 1030 1031 1032 1033
1024 2048 3072

Explanation:

Example case 1: In the array 1 2 3 4 5 6 7 8 9 10
                file sizes are 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
                1's count in their binary representation are 1, 1, 2, 1, 2, 2, 3, 1, 2, 2
                So sorted array is 1 2 4 8 3 5 6 9 10 7

"""

import math as m
from sys import stdin, stdout


def convert_to_file_size(arr):
    """
    :param arr: Array input given by the user
    :return: An integer array consisting of file sizes corresponding to arr
    """
    arr1 = []
    for num in arr:
        if num == 0:
            arr.append(0)
        else:
            i = int(m.floor(m.log(num, 1024)))
            power = m.pow(1024, i)
            size = int(num / power)
            arr1.append(size)
    return arr1


def count_of_binary_1s(arr):
    """
    :param arr: Array returned by convert_to_file_size()
    :return: An integer array consisting of count of no.of 1's in array's binary representation
    """
    arr1 = []
    for num in arr:
        if num == 0:
            arr1.append(0)
        else:
            binary = bin(int(num))
            arr1.append(binary[2:len(binary)].count("1"))
    return arr1


def main():
    """
    :return: None
    """
    for _ in range(int(stdin.readline())):
        #size_name = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
        arr_size = int(stdin.readline().strip())
        array = [int(i) for i in stdin.readline().strip().split()]
        arr = convert_to_file_size(array)
        arr1 = count_of_binary_1s(arr)
        sorted_arr = [x for i, x in sorted(zip(arr1, array))]
        for i in range(arr_size):
            stdout.write(str(sorted_arr[i])+" ")
        stdout.write("\n")


if __name__ == "__main__":
    main()
