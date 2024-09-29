from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.']*n for _ in range(n)]
        row, col = [0]*n, [0]*n

        queen_diag_dirs = [(1, 1), (-1, -1), (-1, 1), (1, -1)]

        def getBoardArray(board: List[List[str]]) -> List[str]:
            res = []
            n = len(board)
            for i in range(n):
                s = ""
                for j in range(n):
                    s += board[i][j]
                res.append(s)

            return res
        
        def canPlaceQueen(x: int, y: int) -> bool:
            if row[x] == 1 or col[y] == 1:
                return False
            
            for dx, dy in queen_diag_dirs:
                nx, ny = x+dx, y+dy

                while nx>=0 and ny>=0 and nx<n and ny<n:
                    
                    if board[nx][ny] == 'Q':
                        return False

                    nx = nx+dx
                    ny = ny+dy
            
            return True


        def _solve(x: int):
            
            if x == n:
                res.append(getBoardArray(board))
                return
            
            for ny in range(n):
                if canPlaceQueen(x, ny):
                    board[x][ny] = 'Q'
                    row[x] = col[ny] = 1

                    _solve(x+1)

                    board[x][ny] = '.'
                    row[x] = col[ny] = 0
        
        _solve(0)
        
        return res
    

if __name__ == "__main__":
    s = Solution()
    ans = s.solveNQueens(n=5)
    print(ans)