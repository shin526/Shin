#!/usr/bin/python
# 给定两个字符串 s 和 t，判断 t 是否是 s 的字母异位词，假定只包含小写字母


def isAnagram(s: str, t: str):
    table = [0] * 26
    for i in range(len(s)):
        table[ord(s[i]) - ord('a')] += 1
    # print(table)
    for i in range(len(t)):
        table[ord(t[i]) - ord('a')] -= 1
    # print(table)
    for i in table:
        if i != 0:
            return False
    return True


def isAnagram2(s: str, t: str):
    '''利用python特性'''
    return sorted(s) == sorted(t)


def main():
    s = 'anagram'
    t = 'nagaram'
    print(isAnagram(s, t))
    print(isAnagram2(s, t))


if __name__ == '__main__':
    main()
