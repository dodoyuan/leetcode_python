class Solution:
    def Sum_Solution(self, n):
        # write code here
        return n and (n + self.Sum_Solution(n-1))