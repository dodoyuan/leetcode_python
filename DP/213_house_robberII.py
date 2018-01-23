# After robbing those houses on that street, the thief has found himself
# a new place for his thievery so that he will not get too much attention.
# This time, all houses at this place are arranged in a circle. That means
# the first house is the neighbor of the last one. Meanwhile, the security
# system for these houses remain the same as for those in the previous
# street.

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        if l < 2:
            return nums[0]
        pre_max, pre_premax = nums[1], 0
        for i in nums[2:]:
            rob, not_rob = i + pre_premax, pre_max
            pre_premax, pre_max = pre_max, max(rob, not_rob)
        a = max(pre_max, pre_premax)

        pre_max, pre_premax = nums[0], nums[0]
        for i in nums[2:-1]:
            rob, not_rob = i + pre_premax, pre_max
            pre_premax, pre_max = pre_max, max(rob, not_rob)
        b = max(pre_max, pre_premax)
        return max(a, b)




