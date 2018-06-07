
# -*- coding:utf-8 -*-
# 给你一根长度为n的绳子，请把绳子剪成m段，记每段绳子长度为k[0],k[1]...k[m-1],
# 求k[0]k[1]...k[m-1]的最大值。已知绳子长度n为整数，m>1(至少要剪一刀，
# 不能不剪)，k[0],k[1]...k[m-1]均要求为整数。
# 例如，绳子长度为8时，把它剪成3-3-2，得到最大乘积18；
# 绳子长度为3时，把它剪成2-1，得到最大乘积2。

class Solution:
    def maxCut(self,length):
        if length <= 1:
            return 0
        if length < 4:
            return length - 1
        res = [0] * (length + 1)
        res[1], res[2], res[3] = 1, 2, 3
        for i in range(4, length+1):
            maxTemp = 0
            for j in xrange(1, i/2+1):
                temp = res[j] * res[i-j]
                maxTemp = max(maxTemp, temp)
            res[i] = maxTemp
        return res[length]

if __name__ == '__main__':
    s = Solution()
    print s.maxCut(13)