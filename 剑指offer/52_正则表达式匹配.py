
# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if s is None:
            return
        return self.isMatch(s, 0, pattern, 0)

    def isMatch(self, s, sp, pattern, pp):
        if sp == len(s) and pp == len(pattern):
            return True
        if pp >= len(pattern):
            return False

        if pp < len(pattern) - 1 and pattern[pp+1] == '*':
            if (sp < len(s) and s[sp] == pattern[pp]) or pattern[pp] == '.':
                return self.isMatch(s, sp, pattern, pp+2) or \
                       self.isMatch(s, sp+1, pattern, pp+2) or \
                       self.isMatch(s, sp+1, pattern, pp)
            else:
                return self.isMatch(s, sp, pattern, pp + 2)
        if sp >= len(s):
            return False

        if s[sp] == pattern[pp] or pattern[pp] == '.':
            return self.isMatch(s, sp + 1, pattern, pp + 1)
        return False

s = Solution()
print s.match('bcbbabab', '.*a*a')

class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if len(s) == 0 and len(pattern) == 0:
            return True
        if len(s) > 0 and len(pattern) == 0:
            return False
        if len(pattern) > 1 and pattern[1] == '*':
            if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
                return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
            else:
                return self.match(s, pattern[2:])
        if len(s) > 0 and (pattern[0] == '.' or pattern[0] == s[0]):
            return self.match(s[1:], pattern[1:])
        return False