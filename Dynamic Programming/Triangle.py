from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        def __recursion(i, j):
            if i==n-1:
                return triangle[i][j]
            
            return triangle[i][j] + min(__recursion(i+1, j), __recursion(i+1, j+1))
        
        dp = [[-1]* (i+1) for i in range(n)]
        def __top_down(i, j):
            if i==n-1:
                return triangle[i][j]
            
            if dp[i][j]!=-1:
                return dp[i][j]
            
            dp[i][j] = triangle[i][j] + min(__top_down(i+1, j), __top_down(i+1, j+1))
            return dp[i][j]
        return __top_down(0, 0)
    
    
if __name__ == "__main__":
    s = Solution()
    triangle = [[-10]]
    print(s.minimumTotal(triangle))