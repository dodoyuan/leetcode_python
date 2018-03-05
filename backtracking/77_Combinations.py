# Given two integers n and k, return all possible combinations
# of k numbers out of 1 ... n.
#
# For example,
# If n = 4 and k = 2, a solution is:
#
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]


class Solution(object):
    # TLE
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        def helper( n, start, sub, k, result):
            if k == 0:
                result.append(sub[:])
            for i in xrange(start, n):
                sub.append(i + 1)
                helper(n, i + 1, sub, k - 1, result)
                sub.pop()
        helper(n, 0, [], k, result)
        return result

    # accept
    def combine1(self, n, k):
        ans = []
        stack = []
        x = 1
        while True:
            l = len(stack)
            if l == k:
                ans.append(stack[:])
            if l == k or x > n - k + l + 1:
                if not stack:
                    return ans
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1

