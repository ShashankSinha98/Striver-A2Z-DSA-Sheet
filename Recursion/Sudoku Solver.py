from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        def subSquareInit(x: int) -> int:
            st_x = -1
            if x <= 2:
                st_x = 0
            elif x <= 5:
                st_x = 3
            elif x <= 8:
                st_x = 6
            return st_x
        
        def isPossible(board: List[List[str]], x: int, y: int, val: str) -> bool:
            #print(board)
            for i in range(9):
                if (i != y and board[x][i]==val) or (i != x and board[i][y]==val):
                    return False
            
            st_x, st_y = subSquareInit(x), subSquareInit(y)
            for i in range(st_x, st_x+3):
                for j in range(st_y, st_y+3):
                    if i!=x and j!=y and board[i][j]==val:
                        return False

            return True

        def solve(x: int, y:int):
            if x==9:
                #print(board)
                return True
            
            if y==9:
                return solve(x+1, 0)

            if board[x][y] != '.':
                return solve(x, y+1)
            else:
                for i in range(1, 10):
                    if isPossible(board, x, y, str(i)):
                        #print(x, y, i)
                        board[x][y] = str(i)
                        ans = solve(x, y+1)
                        if ans:
                            return True

                        board[x][y] = '.'
            return False

        solve(0, 0)


if __name__ == "__main__":
    s = Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    s.solveSudoku(board)
    print(board)