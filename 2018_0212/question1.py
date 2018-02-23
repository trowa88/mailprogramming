"""
정수 배열(int array)가 주어지면 가장 큰 이어지는 원소들의 합을 구하시오. 단, 시간복잡도는 O(n).


예제}

Input: [-1, 3, -1, 5]
Output: 7 // 3 + (-1) + 5

Input: [-5, -3, -1]
Output: -1 // -1

Input: [2, 4, -2, -3, 8]
Output: 9 // 2 + 4 + (-2) + (-3) + 8
"""


def arr_sum(arr):
    result = []
    start_index = None
    end_index = len(arr) - 1
    for i, x in enumerate(arr):
        if int(x) > 0 and start_index is None:
            start_index = i
        elif int(x) > 0 and start_index is not None:
            end_index = i
        elif int(x) < 0 and i == len(arr) - 1:
            start_index = i
    result = arr[start_index:end_index+1]
    result_txt = ' + '.join(str(x) if x > 0 else f'({str(x)})' for x in result)
    print(f'Output: {sum(result)} // {result_txt}')


if __name__ == '__main__':
    print('Input: [-1, 3, -1, 5]')
    user_input = [-1, 3, -1, 5]
    arr_sum(user_input)
    print()
    print('Input: [-5, -3, -1]')
    user_input = [-5, -3, -1]
    arr_sum(user_input)
    print()
    print('Input: [2, 4, -2, -3, 8]')
    user_input = [2, 4, -2, -3, 8]
    arr_sum(user_input)
