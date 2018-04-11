
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res = []
        plow, phigh = 1, 2
        while plow < phigh:
            sum = (plow + phigh) * (phigh - plow + 1) >> 1
            if sum < tsum:
                phigh += 1
            elif sum > tsum:
                plow += 1
            else:
                temp = [item for item in range(plow,phigh+1)]
                res.append(temp)
                plow += 1
        return res

s = Solution()
print s.FindContinuousSequence(100)

