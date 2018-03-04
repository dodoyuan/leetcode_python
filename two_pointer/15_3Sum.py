class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, length = [], len(nums)
        if length < 3:
            return res
        nums = sorted(nums)
        for i in xrange(length-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            temp = 0 - nums[i]
            left, right = i + 1, length - 1
            while left < right:
                if nums[left] + nums[right] == temp:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    right -= 1
                    left += 1
                elif nums[left] + nums[right] > temp:
                    right -= 1
                else:
                    left += 1
        return res

if __name__ == '__main__':
    s = Solution()
    print s.threeSum([-1, 0, 1, 2, -1, -4])
