from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        def __recursion(i, buy, t):
            if i==n or t==0:
                return 0
            
            if buy:
                return max(-prices[i]+__recursion(i+1, False, t), __recursion(i+1, True, t))
            else:
                return max(prices[i]+__recursion(i+1, True, t-1), __recursion(i+1, False, t))

        n = len(prices)
        dp = [[[-1, -1, -1], [-1,-1,-1]] for _ in range(n)]
        def __top_down(i, buy, t):
            if i==n or t==0:
                return 0
            
            if dp[i][buy][t]!=-1:
                return dp[i][buy][t]

            if buy:
                dp[i][buy][t] = max(-prices[i]+__top_down(i+1, 0, t), __top_down(i+1, 1, t))
            else:
                dp[i][buy][t] = max(prices[i]+__top_down(i+1, 1, t-1), __top_down(i+1, 0, t))
            return dp[i][buy][t]
        
        return __top_down(0, 1, 2)


if __name__ == "__main__":
    s = Solution()
    p = [3,3,5,0,0,3,1,4]
    print(s.maxProfit(p))