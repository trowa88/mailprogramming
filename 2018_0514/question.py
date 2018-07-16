"""
문자열 배열(string array)이 주어지면, 제일 긴 공통된 접두사(prefix)의 길이를 찾으시오.

예제)
Input: [“apple”, “apps”, “ape”]
Output: 2 // “ap”

Input: [“hawaii”, “happy”]
Output: 2 // “ha”

Input: [“dog”, “dogs”, “doge”]
Output: 3 // “dog”
"""


def find_prefix(word_list):
    prefix = ''
    result = 0
    word = word_list.pop()

    for i, ch in enumerate(word):
        involve = True
        for tmp in word_list:
            if i + 1 > len(tmp) or ch != tmp[i]:
                involve = False
                break
        if involve:
            prefix += ch
            result += 1
    print(f'{result} // {prefix}')


find_prefix(['apple', 'apps', 'ape'])
find_prefix(['hawaii', 'happy'])
find_prefix(['dog', 'dogs', 'doge'])
