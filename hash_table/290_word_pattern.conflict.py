# >Given a pattern and a string str, find if str follows the same
# pattern.
# Here follow means a full match, such that there is a bijection
# between a letter in pattern and a non-empty word in str.
# Examples:
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.

from itertools import izip

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(' ')
        print words
        if len(pattern) != len(words):
            return False

        p2w, w2p = {}, {}
        for p, w in izip(pattern,words):
            if p not in p2w and w not in w2p:
                p2w[p] = w
                w2p[w] = p
            else:
                if w not in w2p or w2p[w] != p:
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    print s.wordPattern('abba', "dog cat cat dog")