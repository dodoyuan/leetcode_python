


from collections import defaultdict
class Solution:
    lookup = defaultdict(int)
    def Fibonacci(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if self.lookup[n]:
            return self.lookup[n]
        else:
            temp = self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
            self.lookup[n] = temp
        return self.lookup[n]

s = Solution()
print s.Fibonacci(7)