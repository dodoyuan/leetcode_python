
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        result = []
        i = 0
        j = 0
        median, flag = (len(nums1) + len(nums2))//2, (len(nums1) + len(nums2))%2
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        result += nums1[i:]
        result += nums2[j:]
        if flag == 1:
            return (result[median] + result[median]) * 0.5
        if flag == 0:
            return (result[median - 1] + result[median]) * 0.5


class Solution1(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1, len2 = len(nums1), len(nums2)
        if (len1 + len2) % 2 == 1:
            return self.getKth(nums1, nums2, (len1 + len2)/2 + 1)
        else:
            return (self.getKth(nums1, nums2, (len1 + len2)/2) +
                    self.getKth(nums1, nums2, (len1 + len2)/2 + 1)) * 0.5

    def getKth(self, A, B, k):
        m, n = len(A), len(B)
        if m > n:
            return self.getKth(B, A, k)

        left, right = 0, m
        while left < right:
            mid = left + (right - left) / 2
            if 0 <= k - 1 - mid < n and A[mid] >= B[k - 1 - mid]:
                right = mid
            else:
                left = mid + 1

        Ai_minus_1 = A[left - 1] if left - 1 >= 0 else float("-inf")
        Bj = B[k - 1 - left] if k - 1 - left >= 0 else float("-inf")

        return max(Ai_minus_1, Bj)


# 3 5 7 9 12
# 1 2 4 6 13
# time O(log(min(m,n)))
# space O(1)
class Solution2(object):
    def findMedianSortedArrays(self, nums1, nums2):
        length1, length2 = len(nums1), len(nums2)
        if length1 > length2:
            return self.findMedianSortedArrays(nums2, nums1)
        median, even = (length1 + length2) / 2, (length1 + length2) % 2
        cut1, cut2 = 0, median
        while cut1 <= length1:
            cut2 = median - cut1
            # attention cut - 1 may cross the border
            # L1, L2 = nums1[cut1-1], nums2[cut2-1]
            L1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            L2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            # R1, R2 = nums1[cut1], nums2[cut2]
            R1 = float('inf') if cut1 == length1 else nums1[cut1]
            R2 = float('inf') if cut2 == length2 else nums2[cut2]
            if L1 > R2:
                cut1 -= 1
            elif L2 > R1:
                cut1 += 1
            else:
                if not even:
                    return (max(L1, L2) + min(R1, R2)) * 0.5
                else:
                    return min(R1, R2) * 1.0


if __name__ == '__main__':
    print Solution2().findMedianSortedArrays([1, 3, 5, 7], [2, 4, 6])
    print Solution2().findMedianSortedArrays([1, 2], [3, 4])