
# -*- coding:utf-8 -*-


# 从1到n
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        res = 0
        base = 1
        temp = n

        while n:
            weight = n % 10
            n /= 10
            res += n * base
            if weight > 1:
                res += base
            elif weight == 1:
                res += temp % base + 1
            base *= 10

        return res

s = Solution()
print s.NumberOf1Between1AndN_Solution(1)
