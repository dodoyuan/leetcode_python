# All DNA is composed of a series of nucleotides abbreviated as
# A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it
# is sometimes useful to identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences
# (substrings) that occur more than once in a DNA molecule.
#
# For example,
#
# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
#
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        r, res = [], set()
        for i in xrange(len(s)):
            if len(s[i:]) < 10:
                break
            if s[i + 1:].find(s[i:i + 10]) != -1:
                res.add(s[i:i + 10])

        for item in res:
            r.append(item)

        return r


class Solution2(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res, tempset = set(), set()
        mapdict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        encode = 0
        for i in xrange(len(s)):
            encode = ((encode << 2) + mapdict[s[i]]) & 0xFFFFF
            print encode
            if i < 9:
                continue
            if encode in tempset:
                res.add(s[i-9:i+1])
            else:
                tempset.add(encode)
        return list(res)

if __name__ == '__main__':
    s = Solution2()
    print s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")