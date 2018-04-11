
# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if numbers == []:
            return False
        numbers = sorted(numbers)
        luck_card, i = 0, 0
        while numbers[i] == 0:
            i += 1
        luck_card = i
        for j in xrange(i+1, len(numbers)):
            if numbers[j] == numbers[j-1]:
                return False
            if numbers[j] - numbers[j-1] - 1 > luck_card:
                return False
            else:
                luck_card -= numbers[j] - numbers[j-1] - 1
        return True


if __name__ == '__main__':
    s = Solution()
    print s.IsContinuous([0,0,1,3,5])
