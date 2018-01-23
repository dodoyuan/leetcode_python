# Given a m x n grid filled with non-negative numbers, find a path from top
#  left to bottom right which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        res = [[0 for _ in xrange(n)] for _ in xrange(m)]
        res[0][0] = grid[0][0]
        for i in xrange(1, m):
            res[i][0] = res[i-1][0] + grid[i][0]
        for j in xrange(1, n):
            res[0][j] = res[0][j-1] + grid[0][j]
        for i in xrange(1, m):
            for j in xrange(1, n):
                res[i][j] = min(res[i-1][j], res[i][j-1]) + grid[i][j]

        return res[m-1][n-1]

    def minpathsum2(self,grid):
        '''

        '''
        res = grid[0]
        m, n = len(grid), len(grid[0])
        for j in xrange(1, n):
            res[j] = res[j-1] + grid[0][j]
        for i in xrange(1, m):
            res[0] = res[0] + grid[i][0]
            for j in xrange(1, n):
                res[j] = min(res[j], res[j-1]) + grid[i][j]

        return res[-1]

if __name__ == '__main__':
    s = Solution()
    print s.minPathSum([[1,3,1]])