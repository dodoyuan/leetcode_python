# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# For example,
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X
import collections


# DFS
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        if n == 0:
            return
        for i in xrange(m):
            self.dfs(i,0,board,m,n)
            self.dfs(i,n,board,m,n)
        for j in xrange(n):
            self.dfs(0,j,board,m,n)
            self.dfs(m,j,board,m,n)
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == '1':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


    def dfs(self,i,j,board,m,n):
        if i < 0 or i > m or j < 0 or j > n or board[i][j] != 'O':
            return
        board[i][j] = '1'
        self.dfs(i + 1, j, board, m, n)
        self.dfs(i - 1, j, board, m, n)
        self.dfs(i, j + 1, board, m, n)
        self.dfs(i, j - 1, board, m, n)

# BFS
class Solution2:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if not board:
            return
        q = collections.deque([])

        for i in xrange(len(board)):
            q.append((i, 0))
            q.append((i, len(board[0]) - 1))

        for j in xrange(len(board[0])):
            q.append((0, j))
            q.append((len(board) - 1, j))

        while q:
            i, j = q.popleft()
            if board[i][j] in ['O', 'V']:
                board[i][j] = 'V'
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < len(board) and 0 <= y < len(board[0]) and \
                                    board[x][y] == 'O':
                        board[x][y] = 'V'
                        q.append((x, y))

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] != 'V':
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'

