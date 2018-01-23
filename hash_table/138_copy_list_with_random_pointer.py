# A linked list is given such that each node contains an
# additional random pointer which could point to any node in the
# list or null.
# Return a deep copy of the list.

from collections import defaultdict
# from copy import deepcopy

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        # copy and combine copied list with original list
        current = head
        while current:
            copied = RandomListNode(current.label)
            copied.next = current.next
            current.next = copied
            current = copied.next

        # update random node in copied list
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # split copied list from combined one
        dummy = RandomListNode(0)
        copied_current, current = dummy, head
        while current:
            copied_current.next = current.next
            current.next = current.next.next
            copied_current, current = copied_current.next, current.next
        return dummy.next

# not work till now
class Solution1(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        mapdict = defaultdict(RandomListNode)
        if head is None:
            return None
        listcopy = RandomListNode(head.label)
        copyhead = listcopy
        while head:
            # for copy random
            if head in mapdict.keys():
                mapdict[head].random = listcopy
            mapdict[head.random] = listcopy
            # for copy label
            if head.next:
                next_item = RandomListNode(head.next.label)
                listcopy.next = next_item
                listcopy = listcopy.next

            head = head.next
        listcopy.next = None

        return copyhead

if __name__ == '__main__':
    head = RandomListNode(1)
    head.next = RandomListNode(2)
    head.next.next = RandomListNode(3)
    head.next.next.next = RandomListNode(55)
    s = Solution()
    listcopy = s.copyRandomList(head)
    while listcopy:
        print listcopy.label
        listcopy = listcopy.next

