
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        res = [1 for _ in range(index)]
        k2 = k3 = k5 = 0
        for i in range(1, index):
            res[i] = min(res[k2] * 2, res[k3] * 3, res[k5] * 5)
            if res[i] == res[k2] * 2:
                k2 += 1
            if res[i] == res[k3] * 3:
                k3 += 1
            if res[i] == res[k5] * 5:
                k5 += 1
        return res[-1]
s = Solution()
print s.GetUglyNumber_Solution(7)