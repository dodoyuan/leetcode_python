
# Follow up for "Unique Paths":
# Now consider if some obstacles
# are added to the grids. How many unique paths would there be?
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid == []:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        obstacleGrid[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for j in range(1, n):
            obstacleGrid[0][j] = obstacleGrid[0][j-1] * (1-obstacleGrid[0][j])
        for i in range(1, m):
            obstacleGrid[i][0] = obstacleGrid[i-1][0] * (1-obstacleGrid[i][0])
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[m-1][n-1]

if __name__ == '__main__':
    s = Solution()
    print s.uniquePathsWithObstacles([[1]])
