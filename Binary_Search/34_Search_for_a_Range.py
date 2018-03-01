# Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4]


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = 0, len(nums) - 1
        position = -1
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                position = mid
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        if position == -1:
            return [-1, -1]
        else:
            start, end = position, position
            while nums[start] == target:
                start -= 1
                if start == -1:
                    break
            while nums[end] == target:
                end += 1
                if end == len(nums):
                    break
            return [start+1, end-1]

class Solution1(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None:
            return [-1, -1]
        start = self.findfirst(nums, target)
        end = self.findlast(nums, target)
        return [start, end]

    def findfirst(self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    def findlast(self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1

if __name__ == '__main__':
    s = Solution1()
    print s.searchRange([5,7,7,8,8,10],8)
