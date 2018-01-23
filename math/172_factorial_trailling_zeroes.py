

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res,count = 1, 0
        for item in xrange(1, n+1):
            while item % 5 == 0:
                res *= 5
                item /= 5
            while item % 2 == 0:
                res *= 2
                item /= 2
        while res % 10 == 0:
            res /= 10
            count += 1
        return count

    def trailingZeroes1(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n > 0:
            result += n / 5
            n /= 5
        return result


if __name__ == '__main__':
    s = Solution()
    print s.trailingZeroes1(4660)
