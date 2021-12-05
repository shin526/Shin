#!/usr/bin/python
# 把字符串 s 中的每个空格替换成"%20"
# 双指针法，首先扩充数组到空格替换为"%20"之后的大小，然后从后往前替换，i指向旧长度末尾，j指向新长度末尾


def replaceSpace(s: str):
    spaceCount = s.count(' ')
    res = list(s)
    # 每个空格扩充两个位置
    res.extend([' '] * spaceCount * 2)
    i = len(s) - 1
    j = len(res) - 1
    while i >= 0:
        if res[i] != ' ':
            res[j] = res[i]
            j -= 1
        else:
            res[j - 2:j + 1] = '%20'
            j -= 3
        i -= 1
    return ''.join(res)


def main():
    s = "We are happy."
    print(replaceSpace(s))


if __name__ == '__main__':
    main()
