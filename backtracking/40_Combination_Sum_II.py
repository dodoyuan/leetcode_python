# Given a collection of candidate numbers (C) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.
#
# Each number in C may only be used once in the combination.
#
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates = sorted(candidates)
        self.helper(res, candidates, target, [], 0)
        return res

    def helper(self,res, candidates, target, subres, index):
        if target == 0:
            res.append(subres[:])
        if target < 0:
            return
        for i in xrange(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:
                continue
            subres.append(candidates[i])
            self.helper(res, candidates, target - candidates[i], subres, i + 1)
            subres.pop()

if __name__ == '__main__':
    s = Solution()
    print s.combinationSum2([10,1,2,7,6,1,5],8)