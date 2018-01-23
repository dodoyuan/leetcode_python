# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
#
# Example: 19 is a happy number
#
# 1^2 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        res = n
        while True:
            if 10 < res < 100:
                if res not in s:
                    s.add(res)
                else:
                    return False
            var, res = res, 0
            while var:
                var, temp = var / 10, var % 10
                res += temp * temp
            if res == 1:
                return True


if __name__ == '__main__':
    s = Solution()
    print s.isHappy(19)
