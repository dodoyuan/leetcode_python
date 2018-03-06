# Given n pairs of parentheses, write a function to generate all
# combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.helper('', 0, 0, n)
        return self.res

    def helper(self, s, left, right, n):
        if len(s) == 2 * n:
            self.res.append(s)
            return
        if left < n:
            self.helper(s + '(', left + 1, right, n)
        if left > right:
            self.helper(s + ')', left, right + 1, n)

if __name__ == '__main__':
    s = Solution()
    print s.generateParenthesis(3)