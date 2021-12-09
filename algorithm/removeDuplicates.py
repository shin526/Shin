#!/usr/bin/python
# 给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们
# 在 S 上反复执行重复项删除操作，直到无法继续删除，在完成所有重复项删除操作后返回最终的字符串


def removeDuplicates(s: str):
    stack = []
    for ch in s:
        if stack and ch == stack[-1]:
            stack.pop()
        else:
            stack.append(ch)
    return ''.join(stack)


def main():
    s = 'abcdefghijklmnopqrstuvwxyzzyxwvutsrqponml'
    print(removeDuplicates(s))


if __name__ == '__main__':
    main()
