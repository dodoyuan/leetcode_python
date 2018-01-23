# Given a non-empty string s and a dictionary wordDict containing a
# list of non-empty words, add spaces in s to construct a sentence
# where each word is a valid dictionary word. You may assume the
# dictionary does not contain duplicate words.
#
# Return all such possible sentences.
#
# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].
# A solution is ["cats and dog", "cat sand dog"].

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
