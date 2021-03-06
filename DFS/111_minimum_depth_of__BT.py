# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the
#  root node down to the nearest leaf node.

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.right is None and root.left is None:
            return 1
        if root.right and root.left:
            return min(self.minDepth(root.left), self.minDepth(root.right))
        if root.left:
            return self.minDepth(root.left) + 1
        if root.right:
            return self.minDepth(root.right) + 1

class Solution2(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0 or right == 0:
            return left + right + 1
        else:
            return min(left,right) + 1
