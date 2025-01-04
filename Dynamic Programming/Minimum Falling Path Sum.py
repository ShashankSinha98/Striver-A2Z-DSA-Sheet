from typing import List
import sys

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        def __recursion(i, j):
            if j<0 or j>=n:
                return sys.maxsize
            
            if i==n-1:
                return matrix[i][j]
            
            return matrix[i][j] + min(__recursion(i+1,j-1),__recursion(i+1,j),__recursion(i+1,j+1))
        
        dp = [[-1]*n for _ in range(n)]
        def __top_down(i, j):
            if j<0 or j>=n:
                return sys.maxsize
            
            if i==n-1:
                return matrix[i][j]
            
            if dp[i][j]!=-1:
                return dp[i][j]
            
            dp[i][j] = matrix[i][j] + min(__top_down(i+1,j-1),__top_down(i+1,j),__top_down(i+1,j+1))
            return dp[i][j]
        
        #ans = sys.maxsize
        #for j in range(n):
        #    ans = min(ans, __top_down(0, j))
        #return ans

        def __bottom_up():
            dp = [[-1]*n for _ in range(n)]
            for i in range(n):
                dp[0][i] = matrix[0][i]
            
            for i in range(1, n):
                for j in range(n):
                    left = dp[i-1][j-1] if j-1>=0 else sys.maxsize
                    down = dp[i-1][j]
                    right = dp[i-1][j+1] if j+1<n else sys.maxsize

                    dp[i][j] = matrix[i][j] + min(left, down, right)
            
            return min(dp[-1])
        ans = __bottom_up()
        return ans
    
if __name__ == "__main__":
    s = Solution()
    matrix = [[2,1,3],[6,5,4],[7,8,9]]
    print(s.minFallingPathSum(matrix))

