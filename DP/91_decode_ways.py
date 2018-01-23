# A message containing letters from A-Z is being
# encoded to numbers using the following mapping:
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
# The number of ways decoding "12" is 2.

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '' or s[0] == '0':
            return 0
        if '00' in s:
            return 0
        res = [1 for _ in xrange(len(s))]
        for i, c in enumerate(s):
            if i == 0:
                continue
            if c == '0':
                if s[i-1] > '2':
                    return 0
                else:
                    res[i] = res[i-2]
            else:
                if s[i-1] > '2' or s[i-1] == '0':
                    res[i] = res[i-1]
                elif s[i-1] == '2' and c > '6':
                    res[i] = res[i - 1]
                else:
                    res[i] = res[i-1] + res[i-2]
        return res[-1]

    def numDecodings1(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '' or s[0] == '0':
            return 0
        pre, pre_pre = 1, 0
        for i, c in enumerate(s):
            cur = 0
            if i == 0:
                pre, pre_pre = cur, pre
                continue
            if c != '0':
                cur = pre
            if s[i - 1] == '1' or (s[i - 1] == '2' and c <= '6'):
                cur += pre_pre
            pre, pre_pre = cur, pre

        return pre

    def numDecodings2(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == '0':
            return 0
        prev, prev_prev = 1, 0
        for i in xrange(len(s)):
            cur = 0
            if s[i] != '0':
                cur = prev
            if i > 0 and (s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6')):
                cur += prev_prev
            prev, prev_prev = cur, prev
        return prev

if __name__ == '__main__':
    s = Solution()
    print s.numDecodings1('100')