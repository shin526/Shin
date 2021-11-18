#!/usr/bin/python


class Node:
    __slots__ = ('data', 'next')

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Stack:
    __slots__ = ('top')

    def __init__(self) -> None:
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.isEmpty():
            raise Exception("栈为空")
        item = self.top.data
        self.top = self.top.next
        return item

    def length(self):
        if self.isEmpty():
            raise Exception("栈为空")
        cur = self.top
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def peak(self):
        if self.isEmpty():
            raise Exception("栈为空")
        return self.top.data


def isValid(str):
    '''匹配括号'''
    stack = Stack()
    checkDict = {')': '(', '}': '{', ']': '['}
    for char in str:
        if char in ['(', '[', '{']:
            stack.push(char)
        elif char in [')', '}', ']'] and stack.length() > 0:
            if stack.peak() == checkDict[char]:
                stack.pop()
        else:
            print("匹配失败")

    if stack.isEmpty():
        print("匹配成功")
    else:
        print("匹配失败")


def main():
    s = '{}'
    isValid(s)


if __name__ == '__main__':
    main()
