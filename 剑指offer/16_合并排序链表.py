# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    # 可以进一步优化，不用每次都生成新的节点
    def Merge(self, pHead1, pHead2):
        # write code here
        dummy = ListNode(-1)
        head = dummy
        while pHead1 or pHead2:
            if pHead1 is None:
                dummy.next = ListNode(pHead2.val)
                pHead2, dummy = pHead2.next, dummy.next
                continue
            if pHead2 is None:
                dummy.next = ListNode(pHead1.val)
                pHead1, dummy = pHead1.next, dummy.next
                continue
            if pHead1.val < pHead2.val:
                dummy.next = ListNode(pHead1.val)
                pHead1, dummy = pHead1.next, dummy.next
            else:
                dummy.next = ListNode(pHead2.val)
                pHead2, dummy = pHead2.next, dummy.next
        return head.next