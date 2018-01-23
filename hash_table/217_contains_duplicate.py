# Given an array of integers, find if the array contains
# any duplicates. Your function should return true if any value
# appears at least twice in the array, and it should
# return false if every element is distinct.


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False

class Solution2:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        return len(nums) > len(set(nums))