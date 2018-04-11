
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        sum = 0
        for item in array:
            sum ^= item
        bitset = 1
        while (sum & bitset) == 0:
            bitset = (bitset << 1)
        array1, array2 = [], []
        for item in array:
            if (item & bitset) == 0:
                array1.append(item)
            else:
                array2.append(item)
        num1, num2 = 0, 0
        for a in array1:
            num1 ^= a
        for b in array2:
            num2 ^= b
        return num1, num2

s = Solution()
print s.FindNumsAppearOnce([1,2,3,5,6,2,1,3])