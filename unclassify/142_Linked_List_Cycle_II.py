# Given a linked list, return the node where the cycle begins.
# If there is no cycle, return null.
#


# Note: Do not modify the linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if fast is None or fast.next is None:
            return None
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
