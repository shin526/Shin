#!/usr/bin/python
# 给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符
# 如果剩余字符少于k个，则将剩余字符全部反转,如果剩余字符小于2k但大于或等于k个，则反转前k个字符，其余字符保持原样


def reverseStr(s: str, k: int):
    s = list(s)
    n = len(s)
    i = 0
    while i < n:
        start = i
        end = min(n - 1, start + k - 1)
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        i += k * 2
    return ''.join(s)


def main():
    s = "abcdefg"
    print(reverseStr(s, 2))


if __name__ == '__main__':
    main()
