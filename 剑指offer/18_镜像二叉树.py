# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root is None:
            return None
        mirroot = TreeNode(root.val)
        self.helper(root, mirroot)
        return mirroot

    def helper(self, root1, root2):
        if root1.right:
            root2.left = TreeNode(root1.right.val)
            self.helper(root1.right, root2.left)
        if root1.left:
            root2.right = TreeNode(root1.left.val)
            self.helper(root1.left, root2.right)


class Solution1:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        if root.right:
            self.Mirror(root.right)
        if root.left:
            self.Mirror(root.left)
