# Given a non-negative integer represented as a non-empty array of
# digits, plus one to the integer.
#
# You may assume the integer do not contain any leading zero, except
#  the number 0 itself.
#
# The digits are stored such that the most significant digit is at
# the head of the list.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = digits[::-1]
        carry = 1
        for i in xrange(len(digits)):
            temp = digits[i] + carry
            carry, res = temp / 10, temp % 10
            digits[i] = res
        if carry:
            digits.append(carry)

        return digits[::-1]

if __name__ == '__main__':
    s = Solution()
    print s.plusOne([9,9,9])