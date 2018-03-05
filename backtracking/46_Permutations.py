# Given a collection of distinct numbers,
# return all possible permutations.
#
# For example,
# [1,2,3] have the following permutations:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        sub = []
        self.dfs(nums,sub)
        return self.result

    def dfs(self, nums, sub):
        if len(sub) == len(nums):
            print sub
            self.result.append(sub[:])
        for m in nums:
            if m in sub:
                continue
            sub.append(m)
            self.dfs(nums, sub)
            sub.remove(m)

if __name__ == '__main__':
    s = Solution()
    print s.permute([1,2,3])