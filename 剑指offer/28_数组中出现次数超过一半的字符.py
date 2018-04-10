
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        lookup = {}
        length = len(numbers) / 2
        for item in numbers:
            if lookup.get(item):
                lookup[item] += 1
                if lookup[item] > length:
                    return item
            else:
                lookup[item] = 1
        return 0

    def MoreThanHalfNum_Solution1(self, numbers):
        # write code here
        temp, count = numbers[0], 1
        for item in numbers[1:]:
            if item == temp:
                count += 1
            else:
                count -= 1
                if count == 0:
                    temp = item
                    count = 1
        return temp