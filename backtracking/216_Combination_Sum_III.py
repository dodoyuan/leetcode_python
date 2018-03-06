# Find all possible combinations of k numbers that add up to a number n,
# given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
# Example 1:
#
# Input: k = 3, n = 7
#
# Output:
#
# [[1,2,4]]
#
# Example 2:
#
# Input: k = 3, n = 9
#
# Output:
#
# [[1,2,6], [1,3,5], [2,3,4]]


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.helper(n, k, [], 1)
        return self.res

    def helper(self, n, k, subres, index):
        if k == 0:
            return
        for item in xrange(index,10):
            if item > n:
                break
            subres.append(item)
            if item == n and k == 1:
                self.res.append(subres[:])
            if item < n and k > 1:
                self.helper(n - item, k - 1, subres, item + 1)
            subres.pop()

class Solution1(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.helper(n, k, [], 1)
        return self.res

    def helper(self, n, k, subres, index):
        if k == 0 and n == 0:
            self.res.append(subres[:])
            return
        if k < 0:
            return
        for item in xrange(index, 10):
            if item > n:
                break
            subres.append(item)
            self.helper(n - item, k - 1, subres, item + 1)
            subres.pop()


if __name__ == '__main__':
    s = Solution()
    print s.combinationSum3(2,9)