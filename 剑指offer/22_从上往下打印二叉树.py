
# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root is None:
            return []
        current = [root]
        res = []
        while current:
            nextlevel = []
            for node in current:
                res.append(node.val)
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            current = nextlevel
        return res
