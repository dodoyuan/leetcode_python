
# -*- coding:utf-8 -*-

# 这道题比较重要
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        i = 0
        for item in pushV:
            stack.append(item)
            while stack and stack[-1] == popV[i]:
                stack.pop()
                i += 1
        return stack == []

