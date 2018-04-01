# -*- coding:utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        p, q = pHead, pHead.next
        p.next = None
        while q:
            temp = q.next
            q.next = p
            p, q = q, temp
        return p
