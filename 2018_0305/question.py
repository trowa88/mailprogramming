"""
정수(int)가 주어지면, 팰린드롬(palindrome)인지 알아내시오. 팰린드롬이란, 앞에서부터 읽으나 뒤에서부터 읽으나 같은 단어를 말합니다.
단, 정수를 문자열로 바꾸면 안됩니다.

예제)
Input: 12345
Output: False

Input: -101
Output: False

Input: 11111
Output: True

Input: 12421
﻿Output: True
"""


def check_palindrome(num):
    num_list = []
    reverse_num = 0
    input_num = num
    while num:
        if num < 0:
            print(False)
            return

        num_list.append(num % 10)
        num //= 10

    while len(num_list):
        reverse_num += 10 ** (len(num_list) - 1) * num_list.pop(0)

    print(input_num == reverse_num)


if __name__ == '__main__':
    num = int(input())
    check_palindrome(num)
