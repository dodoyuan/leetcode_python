
# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        self.count = 0
        self.merge_sorted(data)
        return self.count

    def merge_sorted(self,nums):
        if len(nums) == 1:
            return nums
        mid = len(nums) / 2
        left = self.merge_sorted(nums[:mid])
        right = self.merge_sorted(nums[mid:])
        return self.sort(left, right)

    def sort(self, left, right):
        global count
        m, n = len(left), len(right)
        array = []
        i, j = 0, 0
        while i < m and j < n:
            if left[i] <= right[j]:
                array.append(left[i])
                i += 1
            else:
                array.append(right[j])
                j += 1
                self.count += len(left) - i
        array.extend(left[i:])
        array.extend(right[j:])
        return array

s = Solution()
print s.InversePairs([1,4,2,6,2,7])

# -*- coding:utf-8 -*-
class Solution1:
    def InversePairs(self, data):
        # write code here
        self.count = 0
        for item in data[::-1]:
            if item
