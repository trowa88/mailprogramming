"""
주어진 string 에 모든 단어를 거꾸로 하시오.

예제)
Input: “abc 123 apple”
Output: “cba 321 elppa”
"""

s = 'abc 123 apple'
result = ''

s_list = s.split()
for i in s_list:
    result += i[len(i)-1::-1] + ' '

print(result)
