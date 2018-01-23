# Given two arrays, write a function to compute their intersection.
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
#
# Note:
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.

from collections import defaultdict

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        dict1 = defaultdict(int)
        for item in nums1:
            dict1[item] += 1
        for item in nums2:
            if item in dict1:
                res.append(item)
                dict1[item] -= 1
                if dict1[item] == 0:
                    del dict1[item]
        return res

if __name__ == '__main__':
    s = Solution()
    print s.intersect([1,1,2,2],[1,2,2,2])


