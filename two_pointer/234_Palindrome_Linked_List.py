# Given a singly linked list, determine if it is a palindrome.
#
# Follow up:
# Could you do it in O(n) time and O(1) space?


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        if head.next.next is None:
            return head.val == head.next.val
        if head.next.next.next is None:
            return head.val == head.next.next.val
        fast, slow = head.next, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        newHead = slow.next
        slow.next = None
        p = newHead.next
        newHead.next = None
        while p is not None:
            temp = p.next
            p.next = newHead
            newHead, p = p, temp
        while newHead:
            if newHead.val != head.val:
                return False
            newHead, head = newHead.next, head.next
        return True