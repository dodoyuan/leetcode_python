# -*- coding:utf-8 -*-

class Solution1:
    # s字符串
    def isNumeric(self, s):
        # write code here
        self.flag1, self.flag2 = 0, 0
        start = 0
        if s[0] in '+-':
            start += 1
        while start < len(s):
            if s[start] in '+-' and s[start-1] in 'eE':
                start += 1
            if s[start] in '1234567890':
                start += 1
            elif s[start] in 'eE':
                if self.flag1 == 1:
                    return False
                else:
                    self.flag1 = 1
                    start += 1
            elif s[start] == '.' and start > 0 and s[start-1] in '+-1234567890':
                if self.flag2 == 1 or self.flag1 == 1:
                    return False
                else:
                    self.flag2 = 1
                    start += 1
            else:
                return False
        if s[-1] in 'eE.+-':
            return False
        return True
s = Solution1()
print s.isNumeric('-.123')

