# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as a binary
# tree in which the depth of the two subtrees of every node never differ by
# more than 1.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        left = self.getDepth(root.left)
        right = self.getDepth(root.right)
        if abs(left-right) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getDepth(self,root):
        if root is None:
            return 0
        return 1 + max(self.getDepth(root.left), self.getDepth(root.right))

