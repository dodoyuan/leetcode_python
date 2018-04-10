
# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root is None:
            return []
        self.res = []
        self.helper(root, [], expectNumber)
        return self.res

    def helper(self, root, subres, number):
        if number == root.val and root.left is None and root.right is None:
            subres.append(root.val)
            self.res.append(subres[:])
            subres.pop()
            return
        if number < 0:
            return
        if root.left:
            subres.append(root.val)
            self.helper(root.left, subres, number-root.val)
            subres.pop()
        if root.right:
            subres.append(root.val)
            self.helper(root.right, subres, number - root.val)
            subres.pop()
