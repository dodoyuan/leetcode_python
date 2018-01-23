# Given a positive integer n, find the least number of perfect square
# numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given
# n = 13, return 2 because 13 = 4 + 9.
#
# Credits:
# Special thanks to @jianchao.li.fighter for adding this
# problem and creating all test cases.

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in xrange(n+1)]
        for i in xrange(1, n+1):
            numlist = self.subnum(i)
            dp[i] = min(dp[i-num*num] for num in numlist) + 1
        return dp[n]

    def subnum(self, num):
        numlist = []
        for i in xrange(1, num+1):
            if i*i <= num:
                numlist.append(i)
            else:
                return numlist
        return numlist


class Solution1(object):
    dp = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        length = len(self.dp)
        while length < n+1:
            numlist = self.subnum(length)
            temp = min(self.dp[length-num*num] for num in numlist) + 1
            length += 1
            self.dp.append(temp)
        return self.dp[n]

    def subnum(self, num):
        numlist = []
        for i in xrange(1, num+1):
            if i*i <= num:
                numlist.append(i)
            else:
                return numlist
        return numlist


class Solution2(object):
    _num = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = self._num
        while len(num) <= n:
            num += min(num[-i*i] for i in xrange(1, int(len(num)**0.5+1))) + 1,
        return num[n]

if __name__ == '__main__':
    s = Solution1()
    print s.numSquares(13)

