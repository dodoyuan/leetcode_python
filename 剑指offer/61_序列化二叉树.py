
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Serialize(self, root):
        # write code here
        self.pre = []
        self.inorder = []
        self.preFunc(root)
        self.inorderFunc(root)
        return (self.pre, self.inorder)

    def preFunc(self,root):
        if root:
            self.pre.append(root.val)
            self.preFunc(root.left)
            self.preFunc(root.right)

    def inorderFunc(self, root):
        if root:
            self.inorderFunc(root.left)
            self.inorder.append(root.val)
            self.inorderFunc(root.right)

    def Deserialize(self, s):
        # write code here
        preorder, inorder = s[0], s[1]
        return self.buildTree(preorder, inorder)

    def buildTree(self,preorder, inorder):
        if inorder:
            index = inorder.index(preorder[0])
            del preorder[0]
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[:index])
            node.right = self.buildTree(preorder, inorder[index+1:])
            return node