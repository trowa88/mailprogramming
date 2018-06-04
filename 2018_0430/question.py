"""
정수로된 배열이 주어지면, 각 원소가 자신을 뺀 나머지 원소들의 곱셈이 되게하라.

단, 나누기 사용 금지, O(n) 시간복잡도

예제)
input: [1, 2, 3, 4, 5]
output: [120, 60, 40, 30, 24]
"""


def exclude_mul(target):
    arr1 = []
    arr2 = []
    p = 1
    for i, v in enumerate(target):
        arr1.append(p)
        p *= v

    p = 1
    for i, v in enumerate(reversed(target)):
        arr2.append(p)
        p *= v
    arr2 = list(reversed(arr2))

    result = [arr1[i] * arr2[i] for i in range(len(target))]
    print(result)


exclude_mul([1, 2, 3, 4, 5])
