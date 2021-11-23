#!/usr/bin/python
# 删除链表中等于给定值 val 的所有节点

from LinkedList import ListNode, LinkedList


def removeElements(head: ListNode, val):
    while head and head.val == val:
        head = head.next
    cur = head
    while cur and cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head


def main():
    items = [1, 3, 6, 5, 6, 7, 4]
    l1 = LinkedList()
    for item in items:
        l1.addTail(item)
    l1.head = removeElements(l1.head, 6)
    l1.display()


if __name__ == '__main__':
    main()
