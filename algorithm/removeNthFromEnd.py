#!/usr/bin/python
# 删除链表的倒数第n个结点，并且返回链表的头结点,尝试一遍扫描

from LinkedList import ListNode, LinkedList


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    # 虚拟结点指向头结点
    pHead = ListNode(next=head)
    slow, fast = pHead, pHead
    while n > 0:
        fast = fast.next
        n -= 1
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return pHead.next


def main():
    l1 = LinkedList()
    items = [1, 2, 3, 4]
    for item in items:
        l1.addTail(item)
    l1.head = removeNthFromEnd(l1.head, 1)
    l1.display()


if __name__ == '__main__':
    main()
