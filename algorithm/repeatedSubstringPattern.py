#!/usr/bin/python
# 给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。
# 给定的字符串只含有小写英文字母，并且长度不超过10000。


def repeatedSubstringPattern(s: str):

    # 解法一：假设 s 由子串 x 重复 n 次构成，n >= 2，则 s + s 包含 2n 个子串
    # s + s 掐头去尾破坏头尾 2 个子串，得到 s' 包含 2n - 2 个子串，因为 n >= 2
    # 所以至少包含 2 个子串，即 s 至少在 s' 中出现一次
    # 若 n = 1，即子串为本身，s' 不包含 s

    # return s in (s * 2)[1:-1]

    # 解法二：构造next数组，若 next[-1] != 0，则存在最长相等前后缀
    # 如果数组长度可被 数组长度-最长相等前后缀长度 整除，则该字符串有重复子串
    # 数组长度-最长相等前后缀长度 就是一个周期的长度
    n = len(s)
    next = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = next[j - 1]
        if s[i] == s[j]:
            j += 1
        next[i] = j

    if next[-1] != 0 and n % (n - next[-1]) == 0:
        # 重复的子串
        # print(s[:(n - next[-1])])
        return True
    else:
        return False


def main():
    s = 'abcabcabcabc'
    print(repeatedSubstringPattern(s))


if __name__ == '__main__':
    main()
