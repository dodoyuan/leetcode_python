
# >For example:
# Secret number:  "1807"
# Friend's guess: "7810"
# Hint: 1 bull and 3 cows. (The bull is 8, the cows are 0, 1 and 7.)
# Write a function to return a hint according to the secret number and
# friend's guess, use A to indicate the bulls and B to indicate the cows.' \
#       ' In the above example, your function should return "1A3B".

from itertools import izip
from collections import defaultdict

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull, cows = 0, 0
        d1, d2 = defaultdict(int), defaultdict(int)
        for s, g in izip(secret, guess):
            if s == g:
                bull += 1
            else:
                d1[s] += 1
                d2[g] += 1

        for key in d1.keys():
            cows += min(d1[key], d2[key])

        return '%dA%dB' % (bull, cows)

if __name__ == '__main__':
    s = Solution()
    print s.getHint('1122', '2211')