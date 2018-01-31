# OJ's undirected graph serialization:
# Nodes are labeled uniquely.
#
# We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
# As an example, consider the serialized graph {0,1,2#1,2#2,2}.
#
# The graph has a total of three nodes, and therefore contains three parts as separated by #.
#
# First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# Second node is labeled as 1. Connect node 1 to node 2.
# Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
# Visually, the graph looks like the following:
#
#        1
#       / \
#      /   \
#     0 --- 2
#          / \
#          \_/
import Queue
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def __init__(self):
        self.visited = {}
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        newhead = UndirectedGraphNode(node.label)
        self.visited[node] = newhead
        myQueue = Queue.Queue()
        myQueue.put(node)
        while myQueue.qsize():
            current = myQueue.get()
            for neighbor in current.neighbors:
                if neighbor not in self.visited:
                    newnode = UndirectedGraphNode(neighbor.label)
                    myQueue.put(neighbor)
                    self.visited[current].neighbors.append(newnode)
                    self.visited[neighbor] = newnode
                else:
                    self.visited[current].neighbors.append(self.visited[neighbor])

        return newhead

# method 2  DFS
class Solution2(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return None

        return self.dfs(node, {})

    def dfs(self,node,map):
        if node in map:
            return map[node]
        newnode = UndirectedGraphNode(node.label)
        map[node] = newnode

        for neighbor in node.neighbors:
            # if neighbor not in map:
            newnode.neighbors.append(self.dfs(neighbor,map))

        return newnode


