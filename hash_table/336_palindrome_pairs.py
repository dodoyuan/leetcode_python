# Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.
#
# Example 1:
# Given words = ["bat", "tab", "cat"]
# Return [[0, 1], [1, 0]]
# The palindromes are ["battab", "tabbat"]
# Example 2:
# Given words = ["abcd", "dcba", "lls", "s", "sssll"]
# Return [[0, 1], [1, 0], [3, 2], [2, 4]]
# The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res =[]
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words[i+1:], i+1):
                if self.isPalindrome(word1+word2):
                    res.append([i,j])
                if self.isPalindrome(word2+word1):
                    res.append([j,i])
        return res


    def isPalindrome(self,word):
        length = len(word)
        begin, end = 0,length-1
        while begin < end:
            if word[begin] != word[end]:
                return False
            begin += 1
            end -= 1
        return True

if __name__ == '__main__':
    s = Solution()
    print s.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])
