# A binary watch has 4 LEDs on the top which represent the hours (0-11),
# and the 6 LEDs on the bottom represent the minutes (0-59).
#
# Each LED represents a zero or one, with the least significant bit on the right.
#
#
# For example, the above binary watch reads "3:25".
#
# Given a non-negative integer n which represents the number of LEDs that are currently on,
# return all possible times the watch could represent.
#
# Example:
#
# Input: n = 1
# Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        self.res = []
        lookup1, lookup2 = [8,4,2,1], [32,16,8,4,2,1]
        for i in xrange(num+1):
            res1, res2 = [], []
            self.helper(lookup1, i, res1, 0)
            self.helper(lookup2, num - i, res2, 0)
            for item in res1:
                if item >= 12:
                    continue
                for value in res2:
                    if value >= 60:
                        continue
                    else:
                        temp = str(value) if value >= 10 else '0' + str(value)
                        self.res.append(str(item) + ':' + temp)
        return self.res

    def helper(self, lookup, count, res, subres):
        if count == 0:
            res.append(subres)
            return
        for i in xrange(len(lookup)):
            subres += lookup[i]
            self.helper(lookup[i+1:], count-1, res, subres)
            subres -= lookup[i]

if __name__ == '__main__':
    s = Solution()
    print s.readBinaryWatch(1)