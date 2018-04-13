
# -*- coding:utf-8 -*-

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        slow, fast = 0, 0
        while True:
            slow = numbers[slow]
            temp = numbers[fast]
            fast = numbers[temp]
            if slow == fast:
                break
        fast = 0
        while slow != fast:
            slow = numbers[slow]
            fast = numbers[fast]
        duplication = slow
        return True

# 上面的程序还是有点问题，就是没有环时也会出现循环

class Solution1:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        lookup = {}
        for item in numbers:
            if lookup.get(item):
                duplication[0] = item
                return True
            else:
                lookup[item] = 1
        return False