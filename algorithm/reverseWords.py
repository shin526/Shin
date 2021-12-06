#!/usr/bin/python
# 给定一个字符串，逐个翻转字符串中的每个单词,输入字符串 s 可以在前面、后面或者单词间包含多余的空格
# 翻转后单词间应当仅用一个空格分隔,不应包含额外的空格


def reverseWords(s: str):
    s = list(s)
    n = len(s)

    # 反转字符串
    def reverseString(s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s

    # 清除多余空格
    def cleanSpace(s):
        i = 0
        j = 0
        end = n
        # 清除末尾空格
        while s[end - 1] == ' ':
            end -= 1
        while j < end:
            # 清除开头和单词间空格
            while j < end and s[j] == ' ':
                j += 1
            # 移动单词
            while j < end and s[j] != ' ':
                s[i] = s[j]
                i += 1
                j += 1
            # 如果没遍历完，单词间添加一个空格
            if j < end:
                s[i] = ' '
                i += 1

        return s[:i]

    reverseString(s, 0, n - 1)
    # print(s)
    s = cleanSpace(s)
    # print(s)

    i = 0
    j = 0
    n = len(s)
    # 反转每个单词
    while j < n:
        while j < n and s[j] != ' ':
            j += 1
        reverseString(s, i, j - 1)
        i, j = j + 1, j + 1
    return ''.join(s)


def main():
    s = "  hello world  "
    print(reverseWords(s))


if __name__ == '__main__':
    main()
