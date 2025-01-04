class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def __recursion(r, c):
            if r==m-1 and c==n-1:
                return 1
            if r>=m or c>=n:
                return 0
            
            return __recursion(r+1, c) +  __recursion(r, c+1)
        
        dp = [[-1]*n for _ in range(m)]
        def __top_down(r, c):
            if r==m-1 and c==n-1:
                return 1
            if r>=m or c>=n:
                return 0
            
            if dp[r][c]!=-1:
                return dp[r][c]
            
            dp[r][c] = __top_down(r+1, c) +  __top_down(r, c+1)
            return dp[r][c]
        return __top_down(0, 0)


if __name__ == "__main__":
    s = Solution()
    m, n = 3, 7
    print(s.uniquePaths(m, n))