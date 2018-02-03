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


# https://www.youtube.com/watch?v=-i2BFAU25Zk
class Solution1(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        rob_rf = [0]*length
        rob_nrf = [0] * length
        nrob_rf = [0] * length
        nrob_nrf = [0] * length
        rob_rf[0] = nums[0]
        for i in xrange(1, length):
            rob_rf[i] = nums[i] + nrob_rf[i-1]
            nrob_rf[i] = max(rob_rf[i-1], nrob_rf[i-1])
            rob_nrf[i] = nums[i] + nrob_nrf[i-1]
            nrob_nrf[i] = max(rob_nrf[i-1], nrob_nrf[i-1])

        return max(nrob_rf[length-1], nrob_nrf[length-1], rob_nrf[length-1])





