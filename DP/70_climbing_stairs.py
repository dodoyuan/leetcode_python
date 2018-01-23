# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        res = [0 for _ in xrange(n+1)]
        res[1] = 1
        res[2] = 2
        for i in xrange(3, n+1):
            res[i] = res[i-1] + res[i-2]
        return res[n]

    def climbStairs2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        a = 1
        b = 2
        for i in xrange(3, n+1):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    s = Solution()
    print s.climbStairs2(4)