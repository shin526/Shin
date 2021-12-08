#!/usr/bin/python
# 仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）
# 只能使用队列的基本操作 —— 也就是 push to back、peek/pop from front、size 和 is empty 这些操作

from collections import deque


class MyStack:
    def __init__(self) -> None:
        self.que1 = deque()  # 存储数据
        self.que2 = deque()  # 出栈临时存放数据

        # 优化后仅用一个队列实现
        # self.que = deque()

    def push(self, x):
        self.que1.append(x)

    def pop(self):
        # 队列1只保留最后一个数据，其他数据全部进入队列2，只能使用popleft()方法
        # 队列1最后一个数据即为栈顶数据，弹出后将队列2数据还原回队列1并清空队列2

        if self.empty():
            return None
        while len(self.que1) > 1:
            self.que2.append(self.que1.popleft())

        res = self.que1.popleft()
        self.que1 = self.que2.copy()
        self.que2.clear()

        return res

        # 只用一个队列时，队尾即为栈顶，将除队尾外的元素全部依次出队然后入队，队尾变为队首，再出队即可
        # for _ in range(len(self.que)-1):
        #     self.que.append(self.que.popleft())
        # return self.que.popleft()

    def top(self):
        if self.empty():
            return None
        else:
            return self.que1[-1]

    def empty(self):
        return not self.que1


def main():
    stack = MyStack()
    print(stack.empty())
    stack.push(1)
    stack.push(2)
    print(stack.top())
    print(stack.pop())
    print(stack.top())
    stack.push(3)
    print(stack.top())
    stack.pop()
    print(stack.empty())
    stack.pop()
    print(stack.empty())


if __name__ == '__main__':
    main()
