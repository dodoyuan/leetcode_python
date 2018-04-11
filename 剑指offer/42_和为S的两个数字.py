
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        start, end = 0, len(array) - 1
        min_produce = float('inf')
        num1, num2 = 0, 0
        while start < end:
            if array[start] + array[end] > tsum:
                end -= 1
            elif array[start] + array[end] < tsum:
                start += 1
            else:
                if array[start] * array[end] < min_produce:
                    min_produce = array[start] * array[end]
                    num1, num2 = array[start], array[end]
                end, start = end - 1, start + 1
        return [] if num1 == num2 else [num1, num2]

s = Solution()
print s.FindNumbersWithSum([1,3,5,6,10,12,13], 15)