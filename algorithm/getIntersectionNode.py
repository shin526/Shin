#!/usr/bin/python
# 给定两个（单向）链表，判定它们是否相交并返回交点。交点不是数值相等，而是指针相等

from LinkedList import ListNode, LinkedList


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    pA, pB = headA, headB
    # 两个指针分别从两个表头开始遍历
    # 两表等长且有交点，则遍历至交点时相等，返回交点，没有交点遍历至末尾时都为None，相等返回None
    # 两表不等长遍历至末尾时从另一表头开始，两表都遍历一次后抵消长度差，继续遍历至交点或末尾返回
    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
    return pA


def main():
    A, B, C, D, E, F, G = [ListNode(x) for x in [1, 2, 3, 4, 5, 2, 1]]
    A.next = B
    B.next = C
    C.next = D
    D.next = E
    G.next = F
    F.next = C

    l1, l2, l3 = LinkedList(), LinkedList(), LinkedList()

    # items = [1, 2, 3, 4]
    # for item in items:
    #     l1.addTail(item)

    # items = [0, 1, 2, 3, 4]
    # for item in items:
    #     l2.addTail(item)

    l1.head = A
    l1.length = 5
    l2.head = G
    l2.length = 5
    l3.head = getIntersectionNode(l1.head, l2.head)
    l3.length = 3
    l1.display()
    l2.display()
    l3.display()
    print(l3.head)


if __name__ == '__main__':
    main()
