# Given a 2D binary matrix filled with 0's and 1's, find the largest
# square containing only 1's and return its area.
# For example, given the following matrix:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Return 4.

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == [] or matrix == [[]]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        maxsquare = 0
        for i in xrange(m):
            matrix[i][0] = int(matrix[i][0])
            if matrix[i][0] == 1:
                maxsquare = 1
        for j in xrange(n):
            matrix[0][j] = int(matrix[0][j])
            if matrix[0][j] == 1:
                maxsquare = 1

        for i in xrange(1, m):
            for j in xrange(1, n):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j]:
                    matrix[i][j] = min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1]) + 1
                    if matrix[i][j] > maxsquare:
                        maxsquare = matrix[i][j]
        return maxsquare**2

if __name__ == '__main__':
    s = Solution()
    l = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    l = [["0","1"],["0","1"]]
    print s.maximalSquare(l)