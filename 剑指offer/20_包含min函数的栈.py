# -*- coding:utf-8 -*-

class Solution:
    def __init__(self):
        self.stack = []
        self.stack2 = []
        self.minim = float("inf")
    def push(self, node):
        # write code here
        self.stack.append(node)
        if node < self.minim:
            self.minim = node
        self.stack2.append(self.minim)
    def pop(self):
        # write code here
        temp = self.stack.pop()
        self.stack2.pop()
        self.minim = self.stack2[len(self.stack2) - 1]
        return temp
    def top(self):
        # write code here
        # return self.stack[len(self.stack)-1]
        return self.stack[-1]
    def min(self):
        # write code here
        return self.minim
s = Solution()
s.push(3)
print s.min
