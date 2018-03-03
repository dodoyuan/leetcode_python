# Given an array of integers that is already sorted in ascending order,
# find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that
#  they add up to the target, where index1 must be less than index2.
# Please note that your returned answers (both index1 and index2)
# are not zero-based.
#
# You may assume that each input would have exactly one solution
# and you may not use the same element twice.
#
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in xrange(len(numbers) - 1):
            if numbers[i] > target:
                break
            temp = self.binary_search(numbers, target - numbers[i], i+1)
            if temp != -1:
                return [i+1, temp+1]
        return [-1, -1]

    def binary_search(self, nums, target, start):
        end =len(nums) - 1
        while start <= end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid - 1
            if nums[mid] < target:
                start = mid + 1
        return -1

if __name__ == '__main__':
    s = Solution()
    print s.twoSum([2,3,4],6)
