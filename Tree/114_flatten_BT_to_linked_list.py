# Given a binary tree, flatten it to a linked list in-place.
#
# For example,
# Given
#
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        res = []
        self.preorderSort(root,res)
        for i in xrange(1,len(res)):
            res[i-1].left = None
            res[i-1].right = res[i]

    def preorderSort(self,root,res):
        if root:
            res.append(root)
            self.preorderSort(root.left,res)
            self.preorderSort(root.right,res)


class Solution1:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        return self.flattenRecu(root, None)

    def flattenRecu(self, root, list_head):
        if root != None:
            list_head = self.flattenRecu(root.right, list_head)
            list_head = self.flattenRecu(root.left, list_head)
            root.right = list_head
            root.left = None
            return root
        else:
            return list_head


class Solution2:
    list_head = None

    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root != None:
            self.flatten(root.right)
            self.flatten(root.left)
            root.right = self.list_head
            root.left = None
            self.list_head = root
            return root
