# -*- coding:utf-8 -*-


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        maxsum, pre_max = float('-inf'), 0
        for item in array:
            if pre_max <= 0:
                pre_max = item
            else:
                pre_max += item
            maxsum = max(pre_max, maxsum)
        return maxsum

s = Solution()
print s.FindGreatestSumOfSubArray([6,-3,-2,7,-15,1,2,2])
