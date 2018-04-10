
# -*- coding:utf-8 -*-


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        lookup = {}
        current, dummy = pHead, RandomListNode(-1)
        cHead = dummy
        # 复制链表，只复制next
        while current:
            node = RandomListNode(current.label)
            lookup[current] = node
            cHead.next = node
            cHead, current = node, current.next

        # 复制random指针
        cHead, current = dummy.next, pHead
        while current:
            cHead.random = lookup.get(current.random)
            cHead, current = cHead.next, current.next
        return dummy.next