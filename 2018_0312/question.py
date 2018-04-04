"""
정수 배열과 타겟 숫자가 주어지면, 합이 타겟값이 되는 두 원소의 인덱스를 찾으시오.
단, 시간복잡도 O(n) 여야 합니다.

예제)
Input: [2, 5, 6, 1, 10], 타겟 8
Output: [0, 2] // 배열[0] + 배열[2] = 8
"""

target_list = [2, 5, 6, 1, 10]
target = 8


def find_index_sum_target(target_list_, target_):
    target_dict = {}
    for i, v in enumerate(target_list_):
        remain = target_ - v
        if remain in target_dict:
            return target_list_.index(remain), i
        target_dict[v] = v
    return -1, -1


a, b = find_index_sum_target(target_list, target)
print(a, b)
