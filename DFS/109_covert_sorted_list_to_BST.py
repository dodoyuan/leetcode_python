# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more
# than 1.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        p_current = head
        val_lsit = []
        while p_current:
            val_lsit.append(p_current.val)
            p_current = p_current.next
        return self.sortedArrayToBST(val_lsit)

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums:
            mid = len(nums) / 2
            node = TreeNode(nums[mid])
            node.left = self.sortedArrayToBST(nums[:mid])
            node.right = self.sortedArrayToBST(nums[mid+1:])
            return node
