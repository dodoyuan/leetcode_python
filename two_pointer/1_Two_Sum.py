

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, item in enumerate(nums):
            if target - item in lookup:
                return [lookup[target-item], i]
            lookup[item] = i
        return [-1, -1]