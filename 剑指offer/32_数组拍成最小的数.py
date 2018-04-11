

# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if numbers == []:
            return ''
        numbers = map(str, numbers)
        self.minnum = '9'
        self.helper(numbers,  0)
        return int(self.minnum)

    def helper(self, numbers, index):
        if index == len(numbers):
            temp = ''.join(numbers)
            if temp < self.minnum:
                self.minnum = temp
            return
        for i in range(index, len(numbers)):
            numbers[index], numbers[i] = numbers[i], numbers[index]
            self.helper(numbers, index + 1)
            numbers[index], numbers[i] = numbers[i], numbers[index]

if __name__ == '__main__':
    s = Solution()
    print s.PrintMinNumber([1,2,3,13])