

class Solution:
    def jumpFloor(self, number):
        if number <= 2:
            return number
        pre,prepre = 2, 1
        for n in xrange(3, number+1):
            pre, prepre = pre + prepre, pre
        return pre