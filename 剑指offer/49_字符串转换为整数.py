
class Solution:
    def StrToInt(self, s):
        # write code here
        if s == '':
            return 0
        i, flag = 0, 1
        while s[i] == ' ':
            i += 1
        if s[i] == '-':
            flag = -1
            i += 1
        elif s[i] == '+':
            i += 1
        res = 0
        for j in range(i,len(s)):
            if s[j] not in '0123456789':
                return 0
            else:
                res = res * 10 + ord(s[j]) - ord('0')
        return flag * res

s = Solution()
print s.StrToInt('-')
