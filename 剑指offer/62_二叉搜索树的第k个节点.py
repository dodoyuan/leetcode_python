
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if k <= 0:
            return
        self.count, self.node = k, None
        self.preorder(pRoot)
        return self.node

    def preorder(self, root):
        if root and self.count:
            self.preorder(root.left)
            self.count -= 1
            if self.count == 0:
                self.node = root
            self.preorder(root.right)