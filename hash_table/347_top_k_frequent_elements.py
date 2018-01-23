# Given a non-empty array of integers, return the k most frequent elements.
#
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].

from collections import defaultdict,Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        lookup = defaultdict(int)
        for item in nums:
            lookup[item] += 1

        sorted_lookup = sorted(lookup.items(), key=lambda item:item[1], reverse=True)
        return [item[0] for item in sorted_lookup[0:k]]

    def topkFrequent1(self,nums,k):
        c = Counter(nums)
        temp = c.most_common(k)
        return [item[0] for item in temp]

if __name__ == '__main__':
    s = Solution()
    print s.topkFrequent1([1,1,1,2,2,3,3,3,3],4)