# Given a list, rotate the list to the right by k places,
# where k is non-negative.
#
#
# Example:
#
# Given 1->2->3->4->5->NULL and k = 2,
#
# return 4->5->1->2->3->NULL.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p = q = head
        length = 0
        while q:
            length += 1
            q = q.next
        k %= length
        if k == 0:
            return head
        slow, fast = head, head
        for i in xrange(k):
            fast = fast.next
        while fast.next is not None:
            slow, fast = slow.next, fast.next
        head = slow.next
        slow.next, fast.next = None, p
        return head

class Solution1(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        n, p = 1, head
        while p.next:
            n += 1
            p = p.next
        p.next = head
        for i in xrange(n - k % n):
            p = p.next
        head = p.next.next
        p.next = None
        return head