# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous
# row.
# For example,
#
# Consider the following matrix:
#
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        if row == 0:
            return False
        cow = len(matrix[0])
        if cow == 0:
            return False
        temp = []
        for i in xrange(row):
            temp.append(matrix[i][cow-1])
        print temp
        res = self.first_not_less_than(temp, target)
        print res
        if res is True:
            return True
        elif res is False:
            return False
        else:
            return self.first_not_less_than(matrix[res], target) is True

    def first_not_less_than(self, nums, target):
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + (end - start) / 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        if nums[start] == target:
            return True
        elif nums[start] > target:
            return start
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],3)
