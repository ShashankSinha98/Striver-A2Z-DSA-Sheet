from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        cboard = [[True]*n for _ in range(m)]
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def solve(x, y, str):
            if len(str) == 0:
                return True
            
            if x<0 or y<0 or x>=m or y>=n or cboard[x][y] == False:
                return False
            
            if board[x][y] != str[0]:
                return False

            cboard[x][y] = False

            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy

                ans = solve(nx, ny, str[1:])
                if ans:
                    return True
            
            cboard[x][y] = True
        

        for x in range(m):
            for y in range(n):
                ans = solve(x, y, word)
                if ans:
                    return True

        return False
    

if __name__ == "__main__":
    s = Solution()
    board = [["A","B","C","E"],["S","F","Z","S"],["A","D","E","E"]]
    word = "ABCESEEDASFZ"

    print(s.exist(board, word))