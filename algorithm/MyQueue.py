#!/usr/bin/python
# 仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）
# 只能使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。


class MyQueue:
    def __init__(self) -> None:
        self.stackIn = []  # 输入栈
        self.stackOut = []  # 输出栈

    def push(self, x):
        self.stackIn.append(x)

    def pop(self):
        if self.empty():
            return None
        # 输出栈为空时，将输入栈所有元素压入输出栈，然后输出栈执行pop
        # 输出栈不为空时，直接pop
        if not self.stackOut:
            while self.stackIn:
                self.stackOut.append(self.stackIn.pop())
        return self.stackOut.pop()

    def peek(self):
        # 取到pop的值后把元素压回输出栈
        res = self.pop()
        self.stackOut.append(res)
        return res

    def empty(self):
        return not (self.stackIn or self.stackOut)


def main():
    myQueue = MyQueue()
    myQueue.push(1)
    myQueue.push(2)
    myQueue.push(3)
    print(myQueue.peek())
    print(myQueue.pop())
    myQueue.push(4)
    print(myQueue.peek())
    print(myQueue.pop())


if __name__ == '__main__':
    main()
