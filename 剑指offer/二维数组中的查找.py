
# -*- coding:utf-8 -*-

# 在一个二维数组中，每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。请完成一个函数，
# 输入这样的一个二维数组和一个整数，判断数组中是否含有该整数

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        m = len(array)
        if m == 0:
            return False
        n = len(array[0])
        if n == 0:
            return False
        i, j = 0, n - 1
        while i < m and j >= 0:
            print array[i][j]
            if array[i][j] == target:
                return True
            elif array[i][j] > target:
                j -= 1
            else:
                i += 1
        return False

if __name__ == '__main__':
    s = Solution()
    print s.Find(1,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])