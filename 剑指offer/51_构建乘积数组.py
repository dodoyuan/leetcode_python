
# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        if len(A) < 2:
            return A
        length = len(A)
        B = [1 for _ in range(length)]
        tempB = [1 for _ in range(length)]
        for i in xrange(1, length):
            B[i] = B[i-1] * A[i-1]
        for j in xrange(length-2, -1, -1):
            tempB[j] = tempB[j+1] * A[j+1]
        for i in xrange(length):
            B[i] *= tempB[i]
        return B

s = Solution()
print s.multiply([1,2,3,4,5])