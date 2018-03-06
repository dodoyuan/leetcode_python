# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# For example,
# If nums = [1,2,2], a solution is:
#
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        nums = sorted(nums)
        self.helper(nums, [], 0)
        return self.res

    def helper(self, nums, subset,start):
        self.res.append(subset[:])
        for i in xrange(start, len(nums)):
            if i != start and nums[i] == nums[i-1]:
                continue
            subset.append(nums[i])
            self.helper(nums, subset, i + 1)
            subset.pop()


if __name__ == '__main__':
    s = Solution()
    print s.subsetsWithDup([1,2,2])