# --*-- coding:utf-8 --*--

#  Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
#
# Note: The input string may contain letters other than the parentheses ( and ).
#
# Example 1:
#
# Input: "()())()"
# Output: ["()()()", "(())()"]
# Example 2:
#
# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]
# Example 3:
#
# Input: ")("
# Output: [""]

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        current = [s]
        visited = set()
        while current:
            nextlevel = []
            for string in current:
                if string in visited:
                    continue
                else:
                    visited.add(string)
                if self.isVaild(string):
                    res.append(string)
                    continue
                for i in range(len(string)):
                    if string[i] not in '()':
                        continue
                    temp = string[:i] + string[i+1:]
                    nextlevel.append(temp)
            if res:
                break
            current = nextlevel
        return res

    def isVaild(self, s):
        if s is None:
            return False
        stack = []
        for char in s:
            if char == '(':
                stack.append('(')
            if char == ')':
                if not stack:
                    return False
                else:
                    stack.pop()

        return stack == []

if __name__ == '__main__':
    s = Solution()
    print s.removeInvalidParentheses(')(')
    print s.isVaild('((()))')