# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# For example, given s = "aab",
# Return
#
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.res = []
        self.helper(s, [], 0)
        return self.res

    def helper(self, s, subres, index):
        if index == len(s):
            self.res.append(subres[:])
            return
        for i in xrange(index, len(s)):
            if self.ispalindrime(s[index:i+1]):
                subres.append(s[index:i+1])
                self.helper(s, subres, i+1)
                subres.pop()



    def ispalindrime(self,s):
        length = len(s)
        left, right = 0, length - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left + 1, right - 1
        return True


if __name__ == '__main__':
    s = Solution()
    print s.partition('aab')