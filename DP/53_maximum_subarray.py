
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
#
# click to show more practice.


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is []:
            return 0
        max_dict = {}
        for i, item in enumerate(nums):
            if i == 0:
                max_dict[i] = item
            else:
                if max_dict[i-1] > 0:
                    max_dict[i] = max_dict[i-1] + item
                else:
                    max_dict[i] = item
        max_num = max(max_dict.values())
        return max_num

    def maxSubArray_v2(self, nums):
        if max(nums) < 0:
            return max(nums)
        global_max,local_max = float('inf'), 0
        for item in nums:
            local_max = max(0, local_max+item)
            global_max = max(global_max, local_max)
        return global_max
