# -*- coding:utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        length1, length2 = 0, 0
        p1, p2 = pHead1, pHead2
        while p1:
            length1 += 1
            p1 = p1.next
        while p2:
            length2 += 1
            p2 = p2.next
        if length1 > length2:
            while length2 < length1:
                pHead1 = pHead1.next
                length1 -= 1
        else:
            while length1 < length2:
                pHead2 = pHead2.next
                length2 -= 1
        while  pHead1 is not pHead2:
            pHead1, pHead2 = pHead1.next, pHead2.next
        return pHead1

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
g = ListNode(7)

a.next = b
b.next = c
c.next = f
f.next = g

d.next = e
e.next = f

s = Solution()
m = s.FindFirstCommonNode(a,d)
print m.val

