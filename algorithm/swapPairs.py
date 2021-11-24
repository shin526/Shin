#!/usr/bin/python
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

from LinkedList import ListNode, LinkedList


def swapPairs(head: ListNode):
    if not head or not head.next:
        return head
    else:
        cur = head.next
        head.next = swapPairs(cur.next)
        cur.next = head
        return cur


def main():
    l1 = LinkedList()
    items = [1, 2, 3, 4]
    for item in items:
        l1.addTail(item)
    l1.head = swapPairs(l1.head)
    l1.display()


if __name__ == '__main__':
    main()
