#! /usr/bin/python


def bf(str1: str, str2: str):
    i, j = 0, 0
    if len(str1) < len(str2):
        return -1

    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0

    if j == len(str2):
        return i - j
    else:
        return -1


def main():
    s1 = 'qweqrtyuiop'
    s2 = ''
    pos = bf(s1, s2)
    print(pos)


if __name__ == '__main__':
    main()
