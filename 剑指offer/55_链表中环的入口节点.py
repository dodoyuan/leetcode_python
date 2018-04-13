
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead is None:
            return None
        fast, slow = pHead, pHead
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break
        if fast is None or fast.next is None:
            return None
        fast = pHead
        while fast != slow:
            fast, slow = fast.next, slow.next
        return slow
