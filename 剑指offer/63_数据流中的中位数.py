
# -*- coding:utf-8 -*-
class Solution:
    sort_list = []
    length = 0

    def Insert(self, num):
        self.sort_list.append(num)
        self.sort_list.sort()
        self.length += 1

    def GetMedian(self,data):
        # write code here
        if self.length % 2:
            return self.sort_list[self.length//2]
        else:
            return self.sort_list[self.length//2] * 0.5 + self.sort_list[self.length//2-1] * 0.5

s = Solution()
for item in [3, 4, 5, 72, 6, 2]:
    s.Insert1(item)
    print s.sort_list