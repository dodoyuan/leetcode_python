# Given an array of integers, every element appears twice
# except for one. Find that single one.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for item in nums:
            res = res ^ item
        return res

if __name__ == '__main__':
    s = Solution()
    print s.singleNumber([7,2,2,4,4,5,5])