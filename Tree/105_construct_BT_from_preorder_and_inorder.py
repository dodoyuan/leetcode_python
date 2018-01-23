# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        lookup = {}
        for i, item in enumerate(inorder):
            lookup[item] = i
        return self.constrctTree(lookup, preorder, inorder, 0, 0, len(inorder))

    def constrctTree(self, lookup, preorder, inorder,pre_start,in_start,in_end):
        if in_start == in_end:
            return None
        node = TreeNode(preorder[pre_start])    # root node
        i = lookup[preorder[pre_start]]
        node.left = self.constrctTree(lookup, preorder, inorder, pre_start+1, in_start, i)
        node.right = self.constrctTree(lookup, preorder, inorder, pre_start + 1 + i - in_start, i+1, in_end)
        return node

class Solution2(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # if inorder:
        #     index = inorder.index(preorder[0])
        #     del preorder[0]
        #     root = TreeNode(inorder[index])
        #     root.left = self.buildTree(preorder, inorder[:index])
        #     root.right = self.buildTree(preorder, inorder[index + 1:])
        #     return root
        if inorder:
            index = inorder.index(preorder[0])
            del preorder[0]
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[:index])
            node.right = self.buildTree(preorder, inorder[index+1:])
            return node



if __name__ ==  "__main__":
    preorder = [1, 2, 4,5,3,6,7]
    inorder = [4,2,5,1,6,3,7]
    result = Solution2().buildTree(preorder, inorder)
    print result.val
    print result.left.val
    print result.right.val





