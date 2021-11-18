#!/usr/bin/python


class Node:
    __slots__ = ('data', 'pre', 'next')

    def __init__(self, data) -> None:
        self.data = data
        self.pre = None
        self.next = None


class DoubleLink:
    __slots__ = ('head')

    def __init__(self) -> None:
        self.head = None

    def clear(self):
        self.__init__()

    def isEmpty(self):
        return self.head is None

    def items(self):
        cur = self.head
        while cur:
            yield cur.data
            cur = cur.next

    def length(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

    def display(self):
        if self.isEmpty():
            print("链表为空")
        else:
            cur = self.head
            while cur:
                if cur.next is None:
                    print(cur.data)
                else:
                    print(f'{cur.data} <-> ', end="")
                cur = cur.next

    def add(self, data):
        '''头部插入结点'''
        node = Node(data)
        if self.isEmpty():
            self.head = node
        else:
            node.next = self.head
            self.head.pre = node
            self.head = node

    def append(self, data):
        '''尾部插入结点'''
        node = Node(data)
        if self.isEmpty():
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            node.pre = cur
            cur.next = node

    def insert(self, index, data):
        '''指定位置插入结点'''
        if index <= 1:
            self.add(data)
        elif index > self.length():
            self.append(data)
        else:
            node = Node(data)
            cur = self.head
            for _ in range(1, index - 1):
                cur = cur.next
            cur.next.pre = node
            node.next = cur.next
            node.pre = cur
            cur.next = node

    def delete(self, index):
        '''删除指定位置结点'''
        cur = self.head
        if self.isEmpty():
            print("链表为空")
            return False
        if index < 1 or index > self.length():
            print("该结点不存在")
            return False
        elif index == 1:
            self.head = cur.next
            # self.head.pre = None
        elif index == self.length():
            while cur.next:
                cur = cur.next
            cur.pre.next = None
        else:
            for _ in range(index - 1):
                cur = cur.next
            cur.pre.next = cur.next
            cur.next.pre = cur.pre

    def find(self, item):
        '''查找元素在链表中的位置'''
        if self.isEmpty():
            print('链表为空')
            return False
        else:
            pos = 1
            cur = self.head
            while cur:
                if cur.data == item:
                    return pos
                cur = cur.next
                pos += 1
            if cur is None:
                print("该结点不存在")
                return False

    def select(self, index: int):
        '''查询指定位置元素'''
        if self.isEmpty() or index < 1 or index > self.length():
            return None
        else:
            pos = 1
            cur = self.head
            while pos < index:
                cur = cur.next
                pos += 1
            return cur.data

    def update(self, index, item):
        '''修改指定位置的元素'''
        if self.isEmpty() or index < 1 or index > self.length():
            print("该结点不存在")
        else:
            pos = 1
            cur = self.head
            while pos < index:
                cur = cur.next
                pos += 1
            cur.data = item


def main():
    l1 = DoubleLink()
    for i in range(5):
        l1.append(i + 1)
    l1.display()
    print(l1.select(0))
    print(l1.select(1))
    print(l1.select(5))
    print(l1.select(6))
    l1.update(3, 10)
    l1.display()


if __name__ == '__main__':
    main()
