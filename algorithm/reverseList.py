#!/usr/bin/python
# 翻转链表

from LinkedList import ListNode, LinkedList


def reverseList(head: ListNode):
    if not head:
        return
    else:
        pre = None
        cur = head
        while cur:
            pre, pre.next, cur = cur, pre, cur.next
        return pre


def reverseList2(head: ListNode):
    if not head or not head.next:
        return head
    else:
        newHead = reverseList2(head.next)
        head.next.next = head
        head.next = None
        return newHead


def main():
    l1 = LinkedList()
    items = [1, 2, 3, 4, 5]
    for item in items:
        l1.addTail(item)
    l1.head = reverseList2(l1.head)
    l1.display()


if __name__ == '__main__':
    main()
