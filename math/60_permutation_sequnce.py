# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.
#
# Note: Given n will be between 1 and 9 inclusive.

from math import factorial

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k -= 1
        res = []
        array = list(range(1,n+1))
        for i in xrange(n,1,-1):
            temp = factorial(i-1)
            a, k = k / temp, k % temp
            res.append(str(array[a]))
            array = array[:a] + array[a+1:]
        res.append(str(array[0]))
        return ''.join(res)

if __name__ == '__main__':
    s = Solution()
    print s.getPermutation(2,2)




