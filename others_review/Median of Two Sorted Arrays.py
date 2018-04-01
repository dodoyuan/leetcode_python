# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1, len2 = len(nums1), len(nums2)
        if (len1 + len2) % 2 == 1:
            return self.getKth(nums1, nums2, (len1 + len2) / 2 + 1)
        else:
            return (self.getKth(nums1, nums2, (len1 + len2) / 2) +
                    self.getKth(nums1, nums2, (len1 + len2) / 2 + 1)) * 0.5

    def getKth(self, nums1, nums2, k):
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.getKth(nums2, nums1, k)

        left, right = 0, m
        while left < right:
            mid = left + (right - left) / 2
            if 0 <= k - 1 - mid < n and nums1[mid] >= nums2[k - 1 - mid]:
                right = mid
            else:
                left = mid + 1
        a = nums1[left - 1] if left - 1 >= 0 else float("-inf")
        b = nums2[k-1-left] if k - 1 - left >= 0 else float("-inf")

        return max(a, b)
