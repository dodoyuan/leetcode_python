

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution2(object):
    def buildTree(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            index = inorder.index(postorder.pop())
            node = TreeNode(inorder[index])
            node.right = self.buildTree(inorder[index+1:], postorder)
            node.left = self.buildTree(inorder[:index], postorder)
            return node

