# Divide two integers without using multiplication, division and mod operator.
#
# If it is overflow, return MAX_INT.

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        count = 0
        if (dividend < 0 and divisor < 0) or (divisor > 0 and dividend > 0):
            flag = 1
        else:
            flag = -1
        divisor, dividend = abs(divisor), abs(dividend)
        for i in xrange(31, -1, -1):
            if (divisor << i) <= dividend:
                count += 2**i
                dividend -= (divisor << i)
        if flag == -1:
            count = -count
        return min(max(-2147483648, count), 2147483647)