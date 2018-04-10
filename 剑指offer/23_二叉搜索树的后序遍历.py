


class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        return self.helper(sequence)

    def helper(self,sequence):
        if len(sequence) == 0:
            return True
        point = sequence[-1]
        i = 0
        while sequence[i] < point:
            i += 1
        less, more = sequence[:i], sequence[i:-1]
        if any(item < point for item in more):
            return False
        else:
            return self.helper(less) and self.helper(more)


if __name__ == '__main__':
    s = Solution()
    print s.VerifySquenceOfBST([2, 4, 3, 6, 7, 8, 5])


