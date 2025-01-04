import sys


class Solution:
    def solve(self, n, m, grid):
        dArr = [-1, 0, 1]
        def __recursion(i, j1, j2):
            if j1<0 or j1>=m or j2<0 or j2>=m:
                return -sys.maxsize
            
            if i==n-1:
                if j1==j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1] + grid[i][j2]
            
            max_choclates = 0
            for dj1 in dArr:
                tmp = 0
                for dj2 in dArr:
                    if j1==j2:
                        tmp = grid[i][j1] + __recursion(i+1, j1+dj1, j2+dj2)
                    else:
                        tmp = grid[i][j1] + grid[i][j2] + __recursion(i+1, j1+dj1, j2+dj2)
                    max_choclates = max(tmp, max_choclates)
            
            return max_choclates
        
        dp = [[[-1]*m for _ in range(m)] for _ in range(n)]
        def __top_down(i, j1, j2):
            if j1<0 or j1>=m or j2<0 or j2>=m:
                return -sys.maxsize
            
            if dp[i][j1][j2]!=-1:
                return dp[i][j1][j2]

            if i==n-1:
                if j1==j2:
                    dp[i][j1][j2] = grid[i][j1]
                else:
                    dp[i][j1][j2] = grid[i][j1] + grid[i][j2]
                return dp[i][j1][j2]
            
            max_choclates = 0
            for dj1 in dArr:
                tmp = 0
                for dj2 in dArr:
                    if j1==j2:
                        tmp = grid[i][j1] + __top_down(i+1, j1+dj1, j2+dj2)
                    else:
                        tmp = grid[i][j1] + grid[i][j2] + __top_down(i+1, j1+dj1, j2+dj2)
                    max_choclates = max(tmp, max_choclates)
            dp[i][j1][j2] = max_choclates
            return max_choclates
        
        def __bottom_up():
            dp = [[[0]*m for _ in range(m)] for _ in range(n)]
            for j1 in range(m):
                for j2 in range(m):
                    if j1==j2:
                        dp[n-1][j1][j2] = grid[n-1][j1]
                    else:
                        dp[n-1][j1][j2] = grid[n-1][j1] + grid[n-1][j2]
            
            for i in range(n-2, -1, -1):
                for j1 in range(m):
                    for j2 in range(m):
                        max_choclates = 0
                        for dj1 in dArr:
                            tmp = 0
                            for dj2 in dArr:
                                if j1+dj1<0 or j1+dj1>=m or j2+dj2<0 or j2+dj2>=m:
                                    tmp = -sys.maxsize
                                elif j1==j2:
                                    tmp = grid[i][j1] + dp[i+1][j1+dj1][j2+dj2]
                                else:
                                    tmp = grid[i][j1] + grid[i][j2] + dp[i+1][j1+dj1][j2+dj2]
                                max_choclates = max(tmp, max_choclates)
                        dp[i][j1][j2] = max_choclates
            
            return dp[0][0][m-1]
        return __bottom_up()


if __name__ == "__main__":
    s = Solution()
    grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
    n, m = 4, 3
    print(s.solve(n, m, grid))
                    
