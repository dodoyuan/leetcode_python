
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot is None:
            return True
        return self.isBalanced(pRoot, float('-inf'), float('inf'))

    def isBalanced(self,root, low, high):
        if root is None:
            return True
        return low < root.val < high and self.isBalanced(root.left, low, root.val) \
               and self.isBalanced(root.right, root.val, high)
