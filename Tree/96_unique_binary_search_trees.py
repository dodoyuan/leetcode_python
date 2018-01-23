class Solution(object):
    _lookup = {0:1, 1:1, 2:2}
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        if n == 2:
            return 2
        res = 0
        for i in xrange(0, n):
            if i in self._lookup:
                a = self._lookup[i]
            else:
                a = self.numTrees(i)
            if n-i-1 in self._lookup:
                b = self._lookup[n-i-1]
            else:
                b = self.numTrees(n-i-1)
            res += a * b
        self._lookup[n] = res
        return res

if __name__ == '__main__':
    s = Solution()
    print s.numTrees(5)