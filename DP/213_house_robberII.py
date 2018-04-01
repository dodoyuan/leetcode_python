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
        if len(nums) < 2:
            return sum(nums)
        # situation 1 rob first
        rob, notrob = nums[0], nums[0]
        for item in nums[2:]:
            rob, notrob = notrob + item, max(rob, notrob)

        # situation 2 notrob first
        rob1, notrob1 = nums[1], 0
        for item in nums[2:]:
            rob1, notrob1 = notrob1 + item, max(rob1, notrob1)
        return max(notrob, rob1, notrob1)





