# -*- coding:utf-8 -*-


# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if ss == '':
            return []
        self.res = set()
        self.helper(list(ss), 0, len(ss))
        return sorted(self.res)

    def helper(self, s, start, end):
        if start > end:
            return
        if start == end:
            self.res.add(''.join(s))
        else:
            for i in range(start, end):
                s[start], s[i] = s[i], s[start]
                self.helper(s, start + 1, end)
                s[start], s[i] = s[i], s[start]



import itertools
class Solution2:
    def Permutation(self, ss):
        # write code here
        result = []
        if not ss:
            return []
        else:
            res = itertools.permutations(ss)
            for i in res:
                if "".join(i) not in result:
                    result.append("".join(i))
        return result

s = Solution()
print s.Permutation('abcc')

