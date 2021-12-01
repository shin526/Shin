#!/usr/bin/python
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null

from LinkedList import ListNode, LinkedList

# slow,fast从头结点开始，fast每次走2步，slow每次走1步，最终在环中相遇
# 头结点距环入口 x ，相遇点距环入口 y ，相遇点距下一次环入口 z，fast在环中走过 n 圈后相遇
# 2(x+y) = x+y+n(y+z) => x = (n-1)(y+z)+z
# 令两个指针分别从头结点和相遇点开始，每次走1步，最终会在环入口相遇


def detectCycle(head: ListNode):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            p = head
            q = slow
            while p != q:
                p = p.next
                q = q.next
            return p
    return None


def main():
    A, B, C, D, E, F, G, H, J = [ListNode(x) for x in range(1, 10)]
    l1 = LinkedList()
    for node in [A, B, C, D, E, F, G, H, J]:
        l1.addNode(node)
    J.next = F
    res = detectCycle(l1.head)
    print(res)
    print(res.val)


if __name__ == '__main__':
    main()
