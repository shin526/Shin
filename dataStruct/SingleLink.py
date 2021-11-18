#! /usr/bin/python


class Node:
    __slots__ = ('_data', '_next')

    def __init__(self, data) -> None:
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data

    @property
    def next(self):
        return self._next

    @data.setter
    def data(self, value):
        self._data = value

    @next.setter
    def next(self, value):
        self._next = value


class SingleLink:
    '''单链表'''
    __slots__ = ('head')

    def __init__(self) -> None:
        self.head = None

    def clear(self):
        self.__init__()

    def isEmpty(self):
        return self.head is None

    def items(self):
        cur = self.head
        while cur is not None:
            yield cur.data
            cur = cur.next

    def display(self):
        if self.isEmpty():
            print("链表为空")
        else:
            for item in self.items():
                print(f'{item} ', end="")
            print("")

    def length(self):
        count = 0
        cur = self.head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def add(self, data):
        '''头部插入结点'''
        node = Node(data)
        self.head, self.head.next = node, self.head

    def append(self, data):
        '''尾部插入结点'''
        node = Node(data)
        if self.isEmpty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
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
            node.next = cur.next
            cur.next = node

    def delete(self, index: int):
        '''删除指定结点'''
        if self.isEmpty():
            print("链表为空")
            return False
        elif index < 1 or index > self.length():
            print("该结点不存在")
            return False

        pre = None
        cur = self.head
        pos = 1
        while cur is not None:
            if index == pos:
                if pre is not None:
                    pre.next = cur.next
                else:
                    self.head = cur.next
                    return True
            pre = cur
            cur = cur.next
            pos += 1

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

    def iterationReverse(self):
        '''迭代法反转链表'''
        if self.isEmpty():
            return
        else:
            pre = None
            cur = self.head
            while cur:
                pre, pre.next, cur = cur, pre, cur.next
            self.head = pre

    def headReverse(self):
        '''头插法反转链表'''
        if self.isEmpty():
            return
        else:
            cur = self.head
            self.head = None
            while cur:
                self.add(cur.data)
                cur = cur.next


class SingleCycleLink:
    __slots__ = ('head')

    def __init__(self) -> None:
        self.head = None


def main():
    l1 = SingleCycleLink()
    for i in range(5):
        l1.append(i + 1)
    l1.display()
    print(l1.select(0))
    print(l1.select(1))
    print(l1.select(5))
    print(l1.select(6))
    l1.update(3, 10)
    l1.display()


if __name__ == "__main__":
    main()
