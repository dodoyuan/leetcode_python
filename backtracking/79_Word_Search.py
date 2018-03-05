# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once.
#
# For example,
# Given board =
#
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        if n == 0 or word is None:
            return False
        visited = [[False for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if self.dfs(board, i, j, visited, word, 0, m, n):
                    return True
        return False

    def dfs(self, board, i, j, visited, word, pos, m, n):
        if pos == len(word):
            return True
        if i < 0 or j < 0 or i >= m or j >= n:
            return False
        if visited[i][j] or board[i][j] != word[pos]:
            return False
        visited[i][j] = True
        res = self.dfs(board, i - 1, j, visited, word, pos + 1, m, n) or \
              self.dfs(board, i + 1, j, visited, word, pos + 1, m, n) or \
              self.dfs(board, i, j - 1, visited, word, pos + 1, m, n) or \
              self.dfs(board, i, j + 1, visited, word, pos + 1, m, n)
        visited[i][j] = False
        return res
