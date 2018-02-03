# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# 11110
# 11010
# 11000
# 00000
# Answer: 1
#
# Example 2:
#
# 11000
# 11000
# 00100
# 00011
# Answer: 3

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        res = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 0:
                    continue
                res += 1
                self.dfs(grid,m,n,i,j)
        return res

    def dfs(self,grid,m,n,i,j):
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        if grid[i][j]:
            grid[i][j] = 0
            self.dfs(grid, m, n, i-1, j)
            self.dfs(grid, m, n, i + 1, j)
            self.dfs(grid, m, n, i, j-1)
            self.dfs(grid, m, n, i, j+1)

def numIslands(self, grid):
    def sink(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
            grid[i][j] = '0'
            map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
            return 1
        return 0
    return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
