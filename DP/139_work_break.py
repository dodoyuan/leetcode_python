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


class Solution1(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        length = len(s)
        if s == '' or length == 1 and s in wordDict:
            return True
        max_len = 0
        for string in wordDict:
            max_len = max(max_len, len(string))
        canBreak = [False for _ in xrange(length)]
        for i in xrange(length):
            left = 0 if i + 1 < max_len else i + 1 - max_len
            for j in xrange(left, i+1):
                if j == 0:
                    if s[0:i+1] in wordDict:
                        canBreak[i] = True
                        break
                else:
                    if s[j:i+1] in wordDict and canBreak[j-1]:
                        canBreak[i] = True
                        break
        return canBreak[-1]

if __name__ == '__main__':
    s = Solution()
    print s.wordBreak('ab',['a', 'b'])