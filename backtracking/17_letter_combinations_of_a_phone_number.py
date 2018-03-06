# Given a digit string, return all possible letter combinations that
# the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
#
#
#
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        self.DigitDict=[' ','1', "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = ['']
        for d in digits:
            res = self.letterCombBT(int(d),res)
        return res

    def letterCombBT(self, digit, oldStrList):
        return [dstr+i for i in self.DigitDict[digit] for dstr in oldStrList]


class Solution1(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        self.res = []
        self.DigitDict = [' ', '1', "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.helper(digits, '', 0)
        return self.res

    def helper(self, digits, subres, index):
        if index == len(digits):
            self.res.append(subres[:])
            return
        for i in self.DigitDict[int(digits[index])]:
            subres += i
            self.helper(digits, subres, index + 1)
            subres = subres[:-1]

if __name__ == '__main__':
    s = Solution1()
    print s.letterCombinations('23')