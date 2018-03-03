# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Write a function to determine if a given target is in the array.
#
# The array may contain duplicates.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if nums == []:
            return False
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[start]:
                if nums[mid] >= target and nums[start] <= target:
                    end = mid
                else:
                    start = mid + 1
            elif nums[mid] < nums[start]:
                if nums[mid] <= target and nums[end] >= target:
                    start = mid
                else:
                    end = mid - 1
            else:
                start += 1
        if nums[start] == target or nums[end] == target:
            return True
        return False