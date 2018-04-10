# -*- coding:utf-8 -*-

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        m = len(matrix)
        if m == 0:
            return None
        n = len(matrix[0])
        if n == 0:
            return None
        res = []
        if m == 1:
            return matrix[0]
        if n == 1:
            return [matrix[item][0] for item in range(m)]
        circle = (min(m, n) - 1) / 2 + 1
        for cir in range(circle):
            for i in range(cir, n-cir):
                res.append(matrix[cir][i])
            for j in range(cir+1, m-cir):
                res.append(matrix[j][n-cir-1])
            for k in range(n-cir-2, cir-1, -1):
                res.append(matrix[m-cir-1][k])
            for h in range(m-cir-2, cir, -1):
                res.append(matrix[h][cir])
        return res


if __name__ == '__main__':
    s = Solution()
    print s.printMatrix([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])