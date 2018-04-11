
# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        count = [0 for _ in range(256)]
        for char in s:
            count[ord(char)] += 1
        for i, char in enumerate(s):
            if count[ord(char)] == 1:
                return i
        return -1