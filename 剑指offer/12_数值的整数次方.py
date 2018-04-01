# -*- coding:utf-8 -*-

class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0:
            return 1
        if exponent < 0:
            temp = self.Power(base, -exponent)
            return 1.0 / temp
        temp = self.Power(base, exponent / 2)
        if temp % 2:
            return temp * temp * base
        else:
            return temp * temp