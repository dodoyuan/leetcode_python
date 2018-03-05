# Given a set of distinct integers, nums,
# return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# For example,
# If nums = [1,2,3], a solution is:
#
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        def dfs(nums, sub, index):
            self.res.append(sub[:])
            for i in xrange(index, len(nums)):
                sub.append(nums[i])
                dfs(nums, sub, i + 1)
                sub.pop()
        dfs(nums, [], 0)
        return self.res

if __name__ == '__main__':
    s = Solution()
    print s.subsets([1,2,3])