# Given a linked list and a value x, partition it such that all nodes
# less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
#
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        dummy1, dummy2 = ListNode(-1), ListNode(-1)
        small, big = dummy1, dummy2
        while head is not None:
            if head.val < x:
                small.next = head
                small, head = small.next, head.next
            else:
                big.next = head
                big, head = big.next, head.next

        small.next = dummy2.next
        big.next = None
        return dummy1.next