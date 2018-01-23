# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        res1, res2 = [], []
        self.preOrdersort(p, res1)
        self.preOrdersort(q, res2)
        if len(res1) != len(res2):
            return False
        for i in xrange(0, len(res1)):
            if res1[i] != res2[i]:
                return False
        return True

    def preOrdersort(self, node, res):
        if node == None:
            res.append(None)
        else:
            res.append(node.val)
            self.preOrdersort(node.left, res)
            self.preOrdersort(node.right,res)


class Solution2:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True

        if p is not None and q is not None:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False