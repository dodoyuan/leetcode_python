# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m, n = len(a), len(b)
        if m > n:
            return self.addBinary(b, a)
        carry, res = 0, ''
        a, b = a[::-1], b[::-1]
        for i in xrange(m):
            temp = int(a[i]) + int(b[i]) + carry
            carry = temp / 2
            res += str(temp % 2)
        for item in b[m:n]:
            temp = int(item) + carry
            carry = temp / 2
            res += str(temp % 2)
        if carry:
            res += str(carry)
        return res[::-1]

if __name__ == '__main__':
    s = Solution()
    print s.addBinary('101111','10')
