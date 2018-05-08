"""
정수 배열(int array)이 주어지면 0이 아닌 정수 순서를 유지하며 모든 0을 배열 오른쪽 끝으로 옮기시오. 단, 시간복잡도는 O(n), 공간복잡도는 O(1)여야 합니다.



예제)

Input: [0, 5, 0, 3, -1]

Output: [5, 3, -1, 0, 0]



Input: [3, 0, 3]

﻿Output: [3, 3, 0]
"""


def zero_move_right(in_list):
    zero_count = 0
    result = []
    for i in in_list:
        if i == 0:
            zero_count += 1
        else:
            result.append(i)
    result += [0 for _ in range(zero_count)]
    return result


# int_list = [0, 5, 0, 3, -1]
int_list = [3, 0, 3]
print(zero_move_right(int_list))
