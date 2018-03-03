# A peak element is an element that is greater than its neighbors.
#
# Given an input array where num[i] != num[i+1], find a peak element and return its index.
#
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
#
# You may imagine that num[-1] = num[n] = -inf.
#
# For example, in array [1, 2, 3, 1], 3 is a peak element and your
# function should return the index number 2.

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start < end:
            mid1 = start + (end - start) / 2
            mid2 = mid1 + 1
            if nums[mid1] < nums[mid2]:
                start = mid2
            else:
                end = mid1
        return start