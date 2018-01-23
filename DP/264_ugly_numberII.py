# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include
# 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
#
# Note that 1 is typically treated as an ugly number, and n
# does not exceed 1690.

import heapq

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        uglynum = [1 for _ in xrange(n)]
        i = 0
        k2 = k3 = k5 = 0
        while i < n-1:
            minnum = min(uglynum[k2]*2, uglynum[k3]*3, uglynum[k5]*5)
            i += 1
            uglynum[i] = minnum
            if minnum == uglynum[k2]*2:
                k2 += 1
            if minnum == uglynum[k3]*3:
                k3 += 1
            if minnum == uglynum[k5]*5:
                k5 += 1
        return uglynum[n-1]

    def nthUglyNumber1(self, n):
        ugly_number = 0
        heap = []
        heapq.heappush(heap, 1)
        for _ in xrange(n):
            ugly_number = heapq.heappop(heap)
            print ugly_number
            if ugly_number % 2 == 0:
                heapq.heappush(heap, ugly_number * 2)
            elif ugly_number % 3 == 0:
                heapq.heappush(heap, ugly_number * 2)
                heapq.heappush(heap, ugly_number * 3)
            else:
                heapq.heappush(heap, ugly_number * 2)
                heapq.heappush(heap, ugly_number * 3)
                heapq.heappush(heap, ugly_number * 5)

        return ugly_number

if __name__ == '__main__':
    s = Solution()
    print s.nthUglyNumber1(5)