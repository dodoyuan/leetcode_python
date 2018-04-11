

class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if s == '':
            return ''
        length = len(s)
        n %= length
        return s[n:] + s[:n]


s = Solution()
print s.LeftRotateString('abcdefgh', 2)