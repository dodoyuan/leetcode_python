

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n >= 0:
            while n:
                count += (n & 1)
                n = (n >> 1)
        else:
            n = ~n
            while n:
                count += (n & 1)
                n = (n >> 1)
            count = 32 - count
        return count

if __name__ == '__main__':
    s = Solution()
    print s.NumberOf1(-15)