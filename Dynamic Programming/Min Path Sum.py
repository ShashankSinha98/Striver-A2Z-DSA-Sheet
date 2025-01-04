from typing import List
import sys

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def __recursion(r, c):
            if r>=m or c>=n:
                return sys.maxsize
            
            if r==m-1 and c==n-1:
                return grid[r][c]
            
            return grid[r][c] + min(__recursion(r+1, c), __recursion(r, c+1))
        
        dp = [[-1]*n for _ in range(m)]
        def __top_down(r, c):
            if r>=m or c>=n:
                return sys.maxsize
            
            if r==m-1 and c==n-1:
                return grid[r][c]
            
            if dp[r][c]!=-1:
                return dp[r][c]
            
            dp[r][c] = grid[r][c] + min(__top_down(r+1, c), __top_down(r, c+1))
            return dp[r][c]
        
        return __top_down(0, 0)
    
if __name__ == "__main__":
    s = Solution()
    grid = [[1,2,3],[4,5,6]]
    print(s.minPathSum(grid))
