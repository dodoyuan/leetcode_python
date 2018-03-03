# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2). 4 5 6 0 1 2 3  4 5
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid

        return min(nums[start], nums[end])

if __name__ == '__main__':
    s = Solution()
    print s.findMin([4,5,6,1,2,3])