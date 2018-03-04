# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
#
# For example,
# Given sorted array nums = [1,1,1,2,2,3],
#
# Your function should return length = 5,
# with the first five elements of nums being 1, 1, 2, 2 and 3.
# It doesn't matter what you leave beyond the new length.
#


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        count = 2
        for i in xrange(2, len(nums)):
            if nums[i] != nums[count-2]:
                nums[count] = nums[i]
                count += 1

        return count

if __name__ == '__main__':
    s = Solution()
    print s.removeDuplicates([1,1,1,2,2,3])