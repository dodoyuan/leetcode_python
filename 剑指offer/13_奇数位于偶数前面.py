# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        even, odd = [], []
        for item in array:
            if item % 2:
                odd.append(item)
            else:
                even.append(item)
        return odd + even
