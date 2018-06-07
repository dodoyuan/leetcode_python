# --*-- coding:utf-8 --*--

class Solution():
    def parChecker(self,parstr):
        if parstr is None or len(parstr) == 1:
            return False
        stack = []
        match = {'[':']','(':')','{':'}'}
        for par in parstr:
            if par in '{[(':
                stack.append(par)
            else:
                if not stack or match.get(stack[-1]) != par:
                    return False
                else:
                    stack.pop()
        return stack == []

if __name__ == '__main__':
    s = Solution()
    print s.parChecker('{[([])]}[][}')
