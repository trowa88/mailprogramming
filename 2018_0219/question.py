"""
피보나치 배열은 0과 1로 시작하며, 다음 피보나치 수는 바로 앞의 두 피보나치 수의 합이 된다.
정수 N이 주어지면, N보다 작은 모든 짝수 피보나치 수의 합을 구하여라.

예제)
Input: N = 12
Output: 10 // 0, 1, 1, 2, 3, 5, 8 중 짝수인 2 + 8 = 10.
"""


def fibonacci_list(n):
    gen = generate_fibonacci()
    result = []
    all_result = []
    while sum(result) <= n:
        generate_number = next(gen)
        if generate_number > n:
            break
        all_result.append(generate_number)
        if generate_number % 2 == 0:
            result.append(generate_number)

    return result, all_result


def generate_fibonacci():
    a = 0
    b = 0
    while True:
        a, b = b, a + b
        yield a
        if b == 0:
            b = 1


if __name__ == '__main__':
    print('Input : ', end='', flush=True)
    user_input = int(input())
    result_list, all_list = fibonacci_list(user_input)
    result_txt1 = ', '.join(str(i) for i in all_list)
    result_txt2 = ' + '.join(str(i) for i in result_list if i != 0)
    print(f'{result_txt1} 중 짝수인 {result_txt2} = {sum(result_list)}')
