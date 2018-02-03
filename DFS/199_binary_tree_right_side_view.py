# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
# For example:
# Given the following binary tree,
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
# You should return [1, 3, 4].

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lookup = {}
        self.dfs(root,0,lookup)
        return lookup.values()


    def dfs(self,root,level,lookup):
        if root:
            if level not in lookup:
                lookup[level] = root.val
        
            self.dfs(root.right,level+1,lookup)
            self.dfs(root.left,level+1,lookup)

if __name__ == '__main__':
    root = TreeNode(1)
    root.right, root.left = TreeNode(2), TreeNode(3)
    s = Solution()
    print s.rightSideView(root)