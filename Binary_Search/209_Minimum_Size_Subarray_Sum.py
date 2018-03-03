# Given an array of n positive integers and a positive integer s,
# find the minimal length of a contiguous subarray of which the sum >= s.
# If there isn't one, return 0 instead.
#
# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        sum, left = 0, 0
        res = float('inf')
        for i in xrange(len(nums)):
            sum += nums[i]
            while sum >= s:
                res = min(res, i-left+1)
                sum -= nums[left]
                left += 1
        return 0 if res == float('inf') else res

if __name__ == '__main__':
    s = Solution()
    print s.minSubArrayLen(7,[2,3,1,2,4,3])
