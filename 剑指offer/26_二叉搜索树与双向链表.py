# -*- coding:utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    flag = 0
    first = None
    pre = None
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree:
            root = pRootOfTree
            self.Convert(pRootOfTree.left)
            if not self.flag:
                self.first = root
                self.pre = self.first
                self.flag = 1
            else:
                self.pre.right = root
                root.left = self.pre
                self.pre = root
                self.pre = root
            self.Convert(root.right)
        return self.first

