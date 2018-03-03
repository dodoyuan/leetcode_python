# Follow up for H-Index: What if the citations array is sorted in ascending
# order? Could you optimize your algorithm?


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length, res = len(citations), 0
        start, end = 0, length - 1
        while start <= end:
            mid = start + (end - start) / 2
            if length - mid <= citations[mid]:
                res = max(length - mid,res)
                end = mid - 1
            else:
                start = mid + 1
        return res

    def hIndex1(self,citations):
        length, res = len(citations), 0
        start, end = 0, length - 1
        while start <= end:
            mid = start + ((end - start) >> 1)
            if length - mid <= citations[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return length - start

if __name__ == '__main__':
    s = Solution()
    print s.hIndex1([0,1,3,5,6])
