"""
길이가 같은 두 문자열(string) A 와 B가 주어지면, A 가 B 로 1:1 암호화 가능한지 찾으시오.

예제)
Input: “EGG”, “FOO”
Output: True // E->F, G->O

Input: “ABBCD”, “APPLE”
Output: True // A->A, B->P, C->L, D->E

Input: “AAB”, “FOO”
Output: False
"""


def is_possible_encrypt(origin, crypt):
    crypt_dict = {}
    if len(origin) != len(crypt):
        return False
    for i, v in enumerate(origin):
        if v not in crypt_dict:
            crypt_dict[v] = crypt[i]
            continue
        if crypt_dict[v] != crypt[i]:
            return False
    return True, crypt_dict


print(is_possible_encrypt('EGG', 'FOO'))
print(is_possible_encrypt('ABBCD', 'APPLE'))
print(is_possible_encrypt('AAB', 'FOO'))
