# Given a non-empty string s and a dictionary wordDict containing
# a list of non-empty words, determine if s can be segmented into
# a space-separated sequence of one or more dictionary words.
# You may assume the dictionary does not contain duplicate words.
#
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
#
# Return true because "leetcode" can be segmented as "leet code".
#
# UPDATE (2017/1/4):
# The wordDict parameter had been changed to a list of strings
# (instead of a set of strings). Please reload the code definition
# to get the latest changes.


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(s) == 1:
            if s in wordDict:
                return True
        if s == '':
            return True
        for i in xrange(1, len(s)+1):
            if s[:i] in wordDict:
                res = self.wordBreak(s[i:], wordDict)
                if res is True:
                    return True
                else:
                    continue
        return False



if __name__ == '__main__':
    s = Solution()
    print s.wordBreak2('ab',['a', 'b'])