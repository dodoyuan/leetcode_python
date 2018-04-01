# For a undirected graph with tree characteristics,
# we can choose any node as the root. The result graph is then a rooted tree.
# Among all possible rooted trees, those with minimum height are called
# minimum height trees (MHTs). Given such a graph,
# write a function to find all the MHTs and return a list of their root labels.
#
# Format
# The graph contains n nodes which are labeled from 0 to n - 1.
# You will be given the number n and a list of undirected edges
# (each edge is a pair of labels).
#
# You can assume that no duplicate edges will appear in edges.
# Since all edges are undirected, [0, 1] is the same as [1, 0]
# and thus will not appear together in edges.
#
# Example 1:
#
# Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]
from collections import defaultdict
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        neighbor = defaultdict(set)
        for u, v in edges:
            neighbor[u].add(v)
            neighbor[v].add(u)
        res, minheight = [], float("inf")
        for i in xrange(n):
            temp = self.height_helper(n, i, neighbor, minheight)
            if temp == minheight:
                res.append(i)
            if temp < minheight:
                res, minheight = [i], temp
        return res

    def height_helper(self, n, node, neighbor, minheight):
        visited = [False for _ in xrange(n)]
        current, height = [node], 0
        while current:
            next_level = []
            for node in current:
                visited[node] = True
                for item in neighbor[node]:
                    if not visited[item]:
                        next_level.append(item)
            current = next_level
            height += 1
            if height > minheight:
                return float("inf")
        return height

if __name__ == '__main__':
    s = Solution()
    print s.findMinHeightTrees(4,[[1,0],[1,2],[1,3]])





