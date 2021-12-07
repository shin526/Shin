#!/usr/bin/python
# 给定两个字符串 haystack 和 needle,haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。
# 如果不存在，则返回-1 。


def kmp(haystack: str, needle: str):
    if not needle:
        return 0

    # 构造next数组
    def getNext(s: str):
        next = [0] * len(s)
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            if s[i] == s[j]:
                j += 1
            next[i] = j
        return next

    next = getNext(needle)
    j = 0
    for i in range(len(haystack)):
        while j > 0 and haystack[i] != needle[j]:
            j = next[j - 1]
        if haystack[i] == needle[j]:
            j += 1
        if j == len(needle):
            return i - j + 1
    return -1


def main():
    haystack = "aaaaa"
    needle = "bba"
    print(kmp(haystack, needle))


if __name__ == '__main__':
    main()
