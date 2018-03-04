# Given an array S of n integers, find three integers in S such that the sum
# is closest to a given number, target. Return the sum of the three integers.
# You may assume that each input would have exactly one solution.
#
#     For example, given array S = {-1 2 1 -4}, and target = 1.
#
#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res, length = -1, len(nums)
        if length < 3:
            return res
        nums.sort()
        res = float("inf")
        for i in xrange(length-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, length - 1
            while left < right:
                temp = nums[i]+nums[left]+nums[right]
                if abs(temp - target) < abs(res - target):
                    res = temp
                if temp > target:
                    right -= 1
                elif temp < target:
                    left += 1
                else:
                    return target
        return res
