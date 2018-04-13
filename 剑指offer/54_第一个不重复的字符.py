
# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    string = ''
    length = 0
    lookup = {}
    def FirstAppearingOnce(self):
        # write code here
        for key in self.string():
            if self.lookup[key] == 1:
                return key
        return '#'

    def Insert(self, char):
        # write code here
        self.string += char
        self.length += 1
        if self.lookup.get(char):
            self.lookup[char] += 1
        else:
            self.lookup[char] = 1