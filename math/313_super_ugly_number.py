# Write a program to find the nth super ugly number.
#
# Super ugly numbers are positive numbers whose all prime factors are
# in the given prime list primes of size k. For example,
# [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the
# first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.
#
# Note:
# (1) 1 is a super ugly number for any given primes.
# (2) The given numbers in primes are in ascending order.
# (3) 0 < k <= 100, 0 < n <= 106, 0 < primes[i] < 1000.
# (4) The nth super ugly number is guaranteed to fit in a 32-bit signed
#  integer.
#
# Credits:
# Special thanks to @dietpepsi for adding this problem and creating all
# test cases.

import heapq

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = 1
        temp = primes
        lenth = len(primes)
        for u in heapq.merge(temp[i] for i in xrange(lenth)):
            if n == 1:
                return ugly
            if u > ugly:
                ugly = u
                n -= 1
                temp = [u * primes[i] for i in xrange(lenth)]

    def nthUglyNumber3(self, n):
        q2, q3, q5 = [2], [3], [5]
        ugly = 1
        for u in heapq.merge(q2, q3, q5):
            if n == 1:
                return ugly
            if u > ugly:
                ugly = u
                n -= 1
                q2 += 2 * u,
                q3 += 3 * u,
                q5 += 5 * u,

if __name__ == '__main__':
    s = Solution()
    print s.nthSuperUglyNumber(10,[2,3,5])
    print s.nthUglyNumber3(10)