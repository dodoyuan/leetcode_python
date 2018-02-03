# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint
# stopping you from robbing each of them is that adjacent houses have
# security system connected and it will automatically contact the police
# if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money
# of each house, determine the maximum amount of money you can rob tonight
# without alerting the police.


# easy understand
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        if l <= 2:
            return max(nums)
        rob, notrob = nums[1], nums[0]
        for i in nums[2:]:
            rob, notrob = i + notrob, max(rob, notrob)
        return max(rob, notrob)

    def rob1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        if l < 2:
            return nums[0]
        pre_max, pre_premax = max(nums[0], nums[1]), nums[0]
        for i in nums[2:]:
            rob, not_rob = i + pre_premax, pre_max
            pre_premax, pre_max = pre_max, max(rob, not_rob)
        return max(pre_max, pre_premax)


    def rob2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now

if __name__ == '__main__':
    s = Solution()
    print s.rob1([4,2,3,8])

