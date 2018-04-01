# -*- coding:utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot2 is None or pRoot1 is None:
            return False
        if pRoot2.val == pRoot1.val:
            if self.issubtree(pRoot1,pRoot2):
                return True
        return self.HasSubtree(pRoot1.left, pRoot2) or \
        self.HasSubtree(pRoot1.right, pRoot2)


    def issubtree(self, root1, root2):
        if root2 is None:
            return True
        if root1 is None and root2 is not None:
            return False
        if root1.val == root2.val:
            return self.issubtree(root1.left, root2.left) and \
                   self.issubtree(root1.right, root2.right)

        