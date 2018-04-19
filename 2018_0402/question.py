"""
정수 배열(int array)이 주어지면 두번째로 큰 값을 프린트하시오.



예제)

Input: [10, 5, 4, 3, -1]

Output: 5



Input: [3, 3, 3]

Output: Does not exist.
"""

numbers = [10, 5, 4, 3, -1]
# numbers = [3, 3, 3]
max_num = max(numbers)

tmp = [i for i in numbers if i < max_num]
if not tmp:
    print('Does not exist.')
else:
    print(max(tmp))
