# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.
#
# For example,
# Given n = 3, your program should return all 5 unique BST's shown
# below.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs(self, start, end):
        if start > end:
            return [None]
        ans = []
        for val in range(start, end + 1):
            leftTree = self.dfs(start, val - 1)
            rightTree = self.dfs(val + 1, end)
            for l in leftTree:
                for r in rightTree:
                    root = TreeNode(val)
                    root.left = l
                    root.right = r
                    ans.append(root)
        return ans

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.dfs(1, n)

if __name__ == '__main__':
    s = Solution()
    print s.generateTrees(3)