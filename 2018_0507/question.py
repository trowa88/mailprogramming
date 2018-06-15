"""
정수 배열(int array)과 정수 N이 주어지면, N 번째로 큰 배열 원소를 찾으시오.
예제)

Input: [-1, 3, -1, 5, 4], 2
Output: 4

Input: [2, 4, -2, -3, 8], 1
Output: 8

Input: [-5, -3, 1], 3
﻿Output: -5
"""


def find_max(num_list, n):
    if n == 1:
        print(max(num_list))
        return
    num_list.pop(num_list.index(max(num_list)))
    find_max(num_list, n - 1)


find_max([-1, 3, -1, 5, 4], 2)
find_max([2, 4, -2, -3, 8], 1)
find_max([-5, -3, 1], 3)
