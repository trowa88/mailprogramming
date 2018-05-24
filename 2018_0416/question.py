"""
String 이 주어지면, 중복된 char 가 없는 가장 긴 서브스트링 (substring)의 길이를 찾으시오.

예제)

Input: “aabcbcbc”
Output: 3 // “abc”


Input: “aaaaaaaa”
Output: 1 // “a”


Input: “abbbcedd”
﻿Output: 4 // “bced”
"""


def search_word(txt):
    result = 0
    start = 0
    char_dict = {}
    for i, c in enumerate(txt):
        if c in char_dict:
            start = max(char_dict.get(c), start)
        result = max(result, i - start + 1)
        char_dict[c] = i + 1
    return result


result_length = search_word('aaaaaaaa')
print(f'{result_length}')
