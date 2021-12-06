#!/usr/bin/python
# 实现字符串左旋转操作的功能,把字符串前面的若干个字符转移到字符串的尾部


def reverseLeftWords(s: str, n: int):
    # 利用切片
    # return s[n:] + s[0:n]

    def reverse(s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s

    s = list(s)
    # 局部反转+整体反转
    reverse(s, 0, n - 1)
    reverse(s, n, len(s) - 1)
    reverse(s, 0, len(s) - 1)
    return ''.join(s)


def main():
    s = "lrloseumgh"
    print(reverseLeftWords(s, 6))


if __name__ == '__main__':
    main()
