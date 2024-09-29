class Solution:
    def findPath(self, board, n):
        res = []

        dirs = {'U':(-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

        def _solve(x, y, curr):
            
            if x<0 or y<0 or x>=n or y>=n or board[x][y]<=0:
                return
            
            if x == n-1 and y == n-1:
                res.append(curr)
                return
            

            board[x][y] = -1

            for k in dirs:
                v = dirs[k]
                dx, dy = v
                nx = x + dx
                ny = y + dy

                curr += k
                _solve(nx, ny, curr)
                curr = curr[:-1]
            
            board[x][y] = 1

        _solve(0, 0, "")
        return res
    

if __name__ == "__main__":
    s = Solution()
    board = [[1, 0, 0],
         [1, 1, 1],
         [1, 0, 1]]
    
    n = len(board)
    ans = s.findPath(board, n)
    print(ans)