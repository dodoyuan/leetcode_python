# Implement pow(x, n).
#
#
# Example 1:
#
# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:
#
# Input: 2.10000, 3
# Output: 9.26100

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n == 0:
            return 1
        if n < 0:
            res = self.myPow(x, -n)
            return 1.0 / res
        temp = self.myPow(x, n / 2)
        if n % 2:
            return temp * temp * x
        else:
            return temp * temp

    def myPow2(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        result = 1
        abs_n = abs(n)
        while abs_n:
            if abs_n & 1:
                result *= x
            abs_n >>= 1
            x *= x

        return 1 / result if n < 0 else result

if __name__ == '__main__':
    s = Solution()
    print s.myPow(2,-4)