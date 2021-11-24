#!/usr/bin/python
# 链表及基本操作


class ListNode:
    __slots__ = ('val', 'next')

    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    '''单链表，索引从0开始'''
    __slots__ = ('head', 'length')

    def __init__(self) -> None:
        self.head = ListNode()
        self.length = 0

    def get(self, index: int):
        '''第index个结点的值，若索引无效返回-1'''
        if index < 0 or index >= self.length:
            return -1
        else:
            cur = self.head
            while index:
                cur = cur.next
                index -= 1
            return cur.val

    def addHead(self, val):
        '''头部插入值为val的结点'''
        node = ListNode(val)
        if self.length == 0:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def addTail(self, val):
        '''尾部插入值为val的结点'''
        node = ListNode(val)
        if self.length == 0:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
        self.length += 1

    def addIndex(self, index: int, val):
        '''在的第index个结点之前添加值为val的结点。
        若index等于链表的长度，则该结点插入到表尾。
        若index大于链表长度，则不会插入节点。
        如果index小于0，则在头部插入节点'''
        if index > self.length:
            return
        if index <= 0:
            self.addHead(val)
        elif index == self.length:
            self.addTail(val)
        else:
            node = ListNode(val)
            cur = self.head
            for _ in range(1, index):
                cur = cur.next
            node.next = cur.next
            cur.next = node
            self.length += 1

    def deleteIndex(self, index):
        '''如果索引有效，删除第index个结点'''
        if index < 0 or index > self.length - 1:
            return
        elif index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            while index > 1:
                cur = cur.next
                index -= 1
            cur.next = cur.next.next
        self.length -= 1

    def display(self):
        if self.length == 0:
            print("链表为空")
        else:
            cur = self.head
            while cur:
                if not cur.next:
                    print(cur.val)
                else:
                    print(f'{cur.val} -> ', end="")
                cur = cur.next


if __name__ == '__main__':
    items = [2]
    l1 = LinkedList()
    for item in items:
        l1.addTail(item)
    l1.deleteIndex(0)
    l1.display()
    print(l1.length)
