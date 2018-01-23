# Given two non-negative integers num1 and num2 represented as
# strings, return the product of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the
# inputs to integer directly.

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        num1, num2 = num1[::-1], num2[::-1]
        res, pre_res = '', ''
        for i in xrange(len(num1)):
            res, carry = '', 0
            res += '0' * i
            for j in num2:
                temp = int(num1[i]) * int(j) + carry
                carry, temp = temp / 10, temp % 10
                res += str(temp)
            if carry:
                res += str(carry)
            pre_res = self.addStr(res, pre_res)

        return pre_res[::-1]

    def addStr(self, list1, list2):
        m, n = len(list1), len(list2)
        assert m >= n
        carry, pre_res = 0, ''
        for i in xrange(n):
            temp = int(list1[i]) + int(list2[i]) + carry
            carry, temp = temp / 10, temp % 10
            pre_res += str(temp)
        for i in list1[n:m]:
            temp = int(i) + carry
            carry, temp = temp / 10, temp % 10
            pre_res += str(temp)
        if carry:
            pre_res += str(carry)

        return pre_res

# The above solution is not efficient, just beat 3% people.
# There a reference answer

class Solution2(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = num1[::-1], num2[::-1]
        res = [0] * (len(num1) + len(num2))
        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                res[i + j] += int(num1[i]) * int(num2[j])
                res[i + j + 1] += res[i + j] / 10
                res[i + j] %= 10

        # Skip leading 0s.
        i = len(res) - 1
        while i > 0 and res[i] == 0:
            i -= 1

        return ''.join(map(str, res[i::-1]))

if __name__ == '__main__':
    s = Solution()
    print s.multiply('999', '999')