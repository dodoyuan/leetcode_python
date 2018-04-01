# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res, current = [], [root]
        while current:
            nextlevel, subres = [], []
            for node in current:
                subres.append(node.val)
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            current = nextlevel
            res.append(subres)
        return res