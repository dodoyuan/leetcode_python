# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        fast, slow = dummy, dummy
        for _ in xrange(k):
            fast = fast.next
            if fast is None:
                return None
        while fast:
            fast, slow = fast.next, slow.next
        return slow
