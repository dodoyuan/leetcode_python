
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 重复的节点不保存
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        head = pHead
        while pHead and pHead.next:
            if pHead.val != pHead.next.val:
                pHead = pHead.next
            else:
                pHead.next = pHead.next.next
        return head

# 删除重复节点，包括本身节点
class Solution1:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        dummy = ListNode(-1)
        dummy.next = pHead
        pre, head = dummy, dummy
        while pHead and pHead.next:
            if pHead.val != pHead.next.val:
                pHead = pHead.next
                pre = pre.next
            else:
                while pHead and pHead.next and pHead.val == pHead.next.val:
                    pHead = pHead.next
                pHead = pHead.next
                pre.next = pHead
        return dummy.next

