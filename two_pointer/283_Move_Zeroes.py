# Given an array nums, write a function to move all 0's to the
# end of it while maintaining the relative order of the non-zero elements.
#
# For example, given nums = [0, 1, 0, 3, 12], after calling your function,
# nums should be [1, 3, 12, 0, 0]


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count, length = 0, len(nums)
        for i in xrange(length):
            if nums[i]:
                nums[count] = nums[i]
                count += 1
        while count <= length - 1:
            nums[count] = 0
            count += 1
        return nums

if __name__ == '__main__':
    s = Solution()
    print s.moveZeroes([0,1,0,3,12])