# Given an array of citations (each citation is a non-negative integer)
# of a researcher,
# write a function to compute the researcher's h-index.
#
# According to the definition of h-index on Wikipedia: "A scientist has
# index h if h of his/her N papers have at least h citations each, and
# the other  N - h papers have no more than h citations each."
#
# For example, given citations = [3, 0, 6, 1, 5], which means the
# researcher has 5 papers in total and each of them had received
# 3, 0, 6, 1, 5 citations respectively. Since the researcher has
# 3 papers with at least 3 citations each and the remaining two with
# no more than 3 citations each, his h-index is 3.
#
# Note: If there are several possible values for h, the maximum one
# is taken as the h-index.

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        if length == 0:
            return 0

        citations = sorted(citations, reverse=True)
        print citations
        h = 0
        for i in xrange(0, length):
            if i == length-1:
                if citations[i] >= i+1:
                    h = i+1
            else:
                if citations[i] >= i+1 and citations[i+1] <= i+1:
                    h = i+1

        return h

    def hIndex2(self, citations):
        length = len(citations)
        if length == 0:
            return 0
        hash_table = [0 for _ in xrange(length+1)]
        for i in xrange(0, length):
            if citations[i] > length:
                hash_table[length] += 1
            else:
                hash_table[citations[i]] += 1

        paper = 0
        for i in xrange(length,-1,-1):
            paper += hash_table[i]
            if paper >= i:
                return i



if __name__ == '__main__':
    s = Solution()
    print s.hIndex2([3,0,6,1,5])

