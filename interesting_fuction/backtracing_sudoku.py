
import sys
from time import sleep

class Suduko():
    def __init__(self, board):
        self.board = board

    def check_all(self,i,j,value):
        return self.check_row(i,j,value) and self.check_column(i,j,value) and self.check_small_zone(i,j,value)

    def check_row(self,i,j,value):
        return value not in self.board[i]

    def check_column(self,i,j,value):
        return value not in [self.board[m][j] for m in xrange(9)]

    def check_small_zone(self,i,j,value):
        num = [self.board[m][n] for m in xrange(i/3*3,(i/3+1)*3)
               for n in xrange(j/3*3,(j/3+1)*3)]
        return value not in num

    def next_point(self):
        for i in xrange(9):
            for j in xrange(9):
                if not self.board[i][j]:
                    return i, j

    def solve(self):
        i, j = self.next_point()
        if i >= 8 and j >= 8:
            return True
        for value in xrange(1, 10):
            if self.check_all(i, j, value):
                self.board[i][j] = value
                if not self.solve():
                    self.board[i][j] = 0
                else:
                    return True

        return False

if __name__ == '__main__':
    s = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 3, 6, 0, 0, 0, 0, 0],
         [0, 7, 0, 0, 9, 0, 2, 0, 0],
         [0, 5, 0, 0, 0, 7, 0, 0, 0],
         [0, 0, 0, 0, 4, 5, 7, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 3, 0],
         [0, 0, 1, 0, 0, 0, 0, 6, 8],
         [0, 0, 8, 5, 0, 0, 0, 1, 0],
         [0, 9, 0, 0, 0, 0, 4, 0, 0]]
    S = Suduko(s)
    S.solve()
    # sleep(0.1)
    # sys.stdout.flush()
    for i in range(9):
        print S.board[i]