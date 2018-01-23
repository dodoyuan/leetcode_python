# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced
# to get t.
#
# All occurrences of a character must be replaced with another
# character while preserving the order of characters. No two characters
#  may map to the same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.

from collections import defaultdict

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        length = len(s)
        dic1, dic2 = defaultdict(list), defaultdict(list)
        for i in xrange(length):
            if s[i] in dic1:
                dic1[s[i]][1] += 1
            else:
                dic1[s[i]] = [i, 1]

            if t[i] in dic2:
                dic2[t[i]][1] += 1
            else:
                dic2[t[i]] = [i, 1]
            if dic2[t[i]] != dic1[s[i]]:
                return False
        return True

from itertools import izip  # Generator version of zip.

class Solution2(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s2t, t2s = {}, {}
        for p, w in izip(s, t):
            if w not in s2t and p not in t2s:
                s2t[w] = p
                t2s[p] = w
            elif w not in s2t or s2t[w] != p:
                # Contradict mapping.
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print s.isIsomorphic('add','bgg')

