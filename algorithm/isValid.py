#!/usr/bin/python
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
# 左括号必须以正确的顺序用相同类型的右括号闭合


def isValid(s: str):

    # 解法一：语法糖
    # while '()' in s or '[]' in s or '{}' in s:
    #     s = s.replace('()', '')
    #     s = s.replace('[]', '')
    #     s = s.replace('{}', '')
    # return not s

    # 解法二：栈
    # stack = []
    # for char in s:
    #     if char == '(':
    #         stack.append(')')
    #     elif char == '[':
    #         stack.append(']')
    #     elif char == '{':
    #         stack.append('}')
    #     elif not stack or char != stack[-1]:
    #         return False
    #     else:
    #         stack.pop()
    # return not stack

    # 解法三：字典
    check = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for char in s:
        if char in check.keys():
            stack.append(check[char])
        elif not stack or char != stack[-1]:
            return False
        else:
            stack.pop()
    return not stack


def main():
    s = '[({}[]))'
    print(isValid(s))


if __name__ == '__main__':
    main()
