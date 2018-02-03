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

