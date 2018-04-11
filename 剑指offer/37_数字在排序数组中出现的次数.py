# -*- coding:utf-8 -*-

class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if data == []:
            return 0
        first = self.getfirst(data,k)
        last = self.getlast(data, k)
        if first == -1 and last == -1:
            return 0
        if first == -1 or last == -1:
            return 1
        else:
            return last - first + 1

    def getfirst(self,data,k):
        start, end = 0, len(data) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if data[mid] < k:
                start = mid + 1
            else:
                end = mid
        if data[start] == k:
            return start
        if data[end] == k:
            return end
        return -1

    def getlast(self,data, k):
        start, end = 0, len(data) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if data[mid] > k:
                end = mid - 1
            else:
                start = mid
        if data[end] == k:
            return end
        if data[start] == k:
            return start
        return -1

s = Solution()
print s.GetNumberOfK([1,2,3,5,5,5,7], 5)