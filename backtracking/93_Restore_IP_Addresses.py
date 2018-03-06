# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# For example:
# Given "25525511135",
#
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res = []
        self.dfs(s, '', 0, 0)
        return self.res

    def dfs(self, s, subres, count, index):
        if count > 4:
            return
        if count == 4 and index == len(s):
            self.res.append(subres)
            return
        for i in xrange(0, 3):
            if index + i + 1 > len(s):
                break
            temp = s[index:index + i + 1]
            if (temp.startswith('0') and len(temp) > 1) or int(temp) >= 256:
                continue
            self.dfs(s, subres + temp + ('' if count == 3 else '.'), count + 1, index + i + 1)

if __name__ == '__main__':
    s = Solution()
    print s.restoreIpAddresses('25525511135')