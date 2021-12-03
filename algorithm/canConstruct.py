#!/usr/bin/python
# 给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，
# 判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面的字符构成。
# 如果可以构成，返回 true ；否则返回 false
# 杂志字符串中的每个字符只能在赎金信字符串中使用一次，假设只包含小写字母


def canConstruct(ransomNote: str, magazine: str) -> bool:
    hashmap = {}
    for letter in ransomNote:
        if letter in hashmap:
            hashmap[letter] += 1
        else:
            hashmap[letter] = 1

    for letter in magazine:
        if letter in hashmap:
            hashmap[letter] -= 1

    for key in hashmap:
        if hashmap[key] > 0:
            return False
    return True


def main():
    ransom = 'aa'
    magazine = 'aab'
    print(canConstruct(ransom, magazine))


if __name__ == '__main__':
    main()
