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
        circle = (min(m,n) - 1) / 2 + 1
        for cir in range(circle):
            for i in range(cir, n-cir):
                res.append(matrix[cir][i])
            for j in range(cir+1,m-cir):
                res.append(matrix[j][n-cir])
            

