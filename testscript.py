
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 2:
            return length
        LIS, maxLIS = [1 for _ in xrange(length)], 1
        for i in xrange(1, length):
            LIS[i] = self.helper(nums[i], LIS[:i], nums)
            maxLIS = max(maxLIS, LIS[i])
        return maxLIS

    def helper(self, num, lis, nums):
        maxlis = 1
        for i, item in enumerate(lis):
            if nums[i] < num:
                maxlis = max(maxlis, item + 1)
        return maxlis


class Solution1(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res = []
        self.helper(s, '', 0, 0)
        return self.res

    def helper(self, s, subres, count, index):
        if count == 4 and index == len(s):
            self.res.append(subres)
        if count > 4:
            return
        for i in range(3):
            if index + i + 1 > len(s):
                break
            temp = s[index:index + i + 1]
            if int(temp) > 255 or (temp.startswith('0') and len(temp) > 1):
                continue
            self.helper(s, subres + temp + ('.' if count < 3 else ''), count + 1, index + i + 1)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution2(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

