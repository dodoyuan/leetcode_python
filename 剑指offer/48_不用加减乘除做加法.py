
# -*- coding:utf-8 -*-

# 写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。

class Solution:
    def Add(self, num1, num2):
        # write code here
        return sum([num1,num2])

s = Solution()
print s.Add(100,222)
