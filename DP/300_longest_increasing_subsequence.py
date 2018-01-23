# Given an unsorted array of integers, find the length of longest
# increasing subsequence.
#
# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101],
# therefore the length is 4. Note that there may be more than
# one LIS combination, it is only necessary for you to return the
# length.
#
# Your algorithm should run in O(n2) complexity.
#
# Follow up: Could you improve it to O(n log n) time complexity?

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 2:
            return length
        res = [1 for _ in xrange(length)]
        maxLIS = 0
        for i in xrange(1, length):
            num = self.searchfirst(nums[:i], nums[i], res)
            res[i] = num + 1
            if res[i] > maxLIS:
                maxLIS = res[i]
        return maxLIS

    def searchfirst(self, nums, item, res):
        num = 0
        for i in xrange(len(nums)):
            if nums[i] < item:
                num = max(num, res[i])
        return num

# Binary search solution.
class Solution1(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LIS = []
        def insert(target):
            left, right = 0, len(LIS) - 1
            # Find the first index "left" which satisfies LIS[left] >= target
            while left <= right:
                mid = left + (right - left) / 2;
                if LIS[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            # If not found, append the target.
            if left == len(LIS):
                LIS.append(target);
            else:
                LIS[left] = target

        for num in nums:
            insert(num)

        return len(LIS)

# Time:  O(n^2)
# Space: O(n)
# Traditional DP solution.
class Solution2(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []  # dp[i]: the length of LIS ends with nums[i]
        for i in xrange(len(nums)):
            dp.append(1)
            for j in xrange(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) if dp else 0

if __name__ == '__main__':
    s = Solution()
    l = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    print s.lengthOfLIS(l)