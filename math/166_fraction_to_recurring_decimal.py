# Given two integers representing the numerator and denominator of
#  a fraction, return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part
# in parentheses.
# For example,
# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == 0 or numerator == 0:
            return '0'
        if (denominator > 0 and numerator > 0) or (denominator < 0 and numerator < 0):
            res = ''
        else:
            res = '-'
        numerator, denominator = abs(numerator), abs(denominator)
        quo, rem = numerator // denominator, numerator % denominator

        if rem == 0:
            res += str(quo)

        else:
            res = res + str(quo) + '.'
            print res

        lookup = {}
        while rem and rem not in lookup:
            lookup[rem] = len(res)
            rem *= 10
            res += str(rem/denominator)
            rem %= denominator

        if rem in lookup:
            res = res[:lookup[rem]] + '(' + res[lookup[rem]:] + ')'

        return res


if __name__ == '__main__':
    s = Solution()
    print s.fractionToDecimal(0,12)
