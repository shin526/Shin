#!/usr/bin/python
# 删除链表中等于给定值 val 的所有节点


class ListNode:
    __slots__ = ('val', 'next')

    def __init__(self, val) -> None:
        self.val = val
        self.next = None


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


def createList():
    A = ListNode(1)
    B = ListNode(1)
    C = ListNode(6)
    D = ListNode(3)
    E = ListNode(1)
    F = ListNode(5)
    G = ListNode(6)
    A.next = B
    B.next = C
    C.next = D
    D.next = E
    E.next = F
    F.next = G
    head = A
    return head


def main():
    head = createList()
    head = removeElements(head, 1)
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next
    print(res)


if __name__ == '__main__':
    main()
