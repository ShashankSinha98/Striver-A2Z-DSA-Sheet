from typing import List
import sys

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        dp = {}
        def __recursion(i, j, n):
            if (i, j, n) in dp:
                return dp[(i, j, n)]
            
            if i==0 and j==0:
                if coins[0][0]>=0 or n==0:
                    dp[(i, j, n)] = coins[0][0]
                else:
                    dp[(i, j, n)] = 0
                    return dp[(i, j, n)]
            
            if i==-1 or j==-1:
                return -sys.maxsize
            
            if (i, j, n) in dp:
                return dp[(i, j, n)]
            
            if coins[i][j]>=0:
                dp[(i, j, n)] = max(__recursion(i-1,j,n), __recursion(i,j-1,n)) + coins[i][j]
            else:
                inc = -sys.maxsize
                if n > 0:
                    inc = max(__recursion(i-1,j,n-1), __recursion(i,j-1,n-1)) 
                exc = max(__recursion(i-1,j,n), __recursion(i,j-1,n))+coins[i][j]
                dp[(i, j, n)] = max(inc, exc)
            return dp[(i, j, n)]
        
        r,c = len(coins), len(coins[0])
        ans = __recursion(r-1, c-1, 2)
        return ans


if __name__ == "__main__":
    s = Solution()
    coins = [[-16,-8],[-6,-3]]
    print(s.maximumAmount(coins))