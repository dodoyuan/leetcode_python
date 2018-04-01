# --*--coding:utf8--

# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
# 请问用n个2*1的小矩形无重叠地覆
# 盖一个2*n的大矩形，总共有多少种方法？

from collections import defaultdict
class Solution:
    lookup = defaultdict(int)
    def rectCover(self, number):
        # write code here
        if number <= 2:
            return number
        if self.lookup[number]:
            return self.lookup[number]
        else:
            res = self.rectCover(number-1) + self.rectCover(number-2)
            self.lookup[number] = res
        return res

s = Solution()
print s.rectCover(4)
