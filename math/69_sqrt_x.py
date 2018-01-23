# Implement int sqrt(int x).
#
# Compute and return the square root of x.
#
# x is guaranteed to be a non-negative integer.

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1 or x == 0:
            return x
        high, low = x,  0
        while low < high:
            middle = (low + high) / 2
            temp = middle * middle
            if temp > x:
                high = middle
            elif temp < x:
                low = middle
            else:
                return middle
            if low + 1 == high:
                return low

if __name__ == '__main__':
    s = Solution()
    print s.mySqrt(2)