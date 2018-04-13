
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []
        current = [pRoot]
        flag = 1
        res = []
        while current:
            nextlevel, subres = [], []
            for node in current:
                subres.append(node.val)
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            current = nextlevel
            res.append(subres if flag else subres[::-1])
            flag = 1 if flag == 0 else 0
        return res

