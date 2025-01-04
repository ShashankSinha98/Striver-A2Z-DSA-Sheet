from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        def __recursion(r, c):
            if r>=m or c>=n or obstacleGrid[r][c]==1:
                return 0
            if r==m-1 and c==n-1:
                return 1
            
            return __recursion(r+1, c) +  __recursion(r, c+1)
        
        dp = [[-1]*n for _ in range(m)]
        def __top_down(r, c):
            if r>=m or c>=n or obstacleGrid[r][c]==1:
                return 0
            if r==m-1 and c==n-1:
                return 1
            
            if dp[r][c]!=-1:
                return dp[r][c]
            
            dp[r][c] = __top_down(r+1, c) +  __top_down(r, c+1)
            return dp[r][c]
        return __top_down(0, 0)
    

if __name__ == "__main__":
    s = Solution()
    og = [[0,0],[0,1]]
    print(s.uniquePathsWithObstacles(og))