# Find the contiguous subarray within an array (containing at
# least one number) which has the largest product.
#
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        max_pro = [0 for _ in xrange(length)]
        min_pro = [0 for _ in xrange(length)]

        for i in xrange(length):
            if i == 0:
                max_pro[i] = nums[i]
                min_pro[i] = nums[i]
            else:
                max_pro[i] = max(max_pro[i - 1] * nums[i], min_pro[i - 1] * nums[i], nums[i])
                min_pro[i] = min(max_pro[i - 1] * nums[i], min_pro[i - 1] * nums[i], nums[i])
        print max_pro, min_pro
        return max(max_pro)

    def maxProduct2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_pro, min_pro, glo_max = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            max_pro, min_pro = max(max_pro * num, min_pro * num, num), \
                               min(max_pro * num, min_pro * num, num)
            if max_pro > glo_max:
                glo_max = max_pro
        return glo_max

    class Solution3:
        # @param A, a list of integers
        # @return an integer
        def maxProduct(self, A):
            global_max, local_max, local_min = float("-inf"), 1, 1
            for x in A:
                local_max = max(1, local_max)
                if x > 0:
                    local_max, local_min = local_max * x, local_min * x
                else:
                    local_max, local_min = local_min * x, local_max * x
                global_max = max(global_max, local_max)
            return global_max


if __name__ == '__main__':
    s = Solution()
    print s.maxProduct2([0])