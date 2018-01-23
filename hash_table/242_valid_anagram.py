class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        ls1, ls2 = [0 for _ in xrange(26)], [0 for _ in xrange(26)]
        for char in s:
            temp = ord(char) - ord('a')
            ls1[temp] += 1

        for char in t:
            temp = ord(char) - ord('a')
            ls2[temp] += 1

        for i in xrange(26):
            if ls1[i] != ls2[i]:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print s.isAnagram('a','a')