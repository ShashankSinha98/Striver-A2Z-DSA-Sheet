from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        def __recursion(i, buy):
            if i==n:
                return 0
            
            if buy:
                return max(-prices[i]+__recursion(i+1, False), __recursion(i+1, True))
            else:
                return max(prices[i]-fee+__recursion(i+1, True), __recursion(i+1, False))


        n = len(prices)
        dp = [[-1]*(2) for _ in range(n)]
        def __top_down(i, buy):
            if i==n:
                return 0
            
            if dp[i][buy]!=-1:
                return dp[i][buy]
            
            if buy==1:
                dp[i][buy] = max(-prices[i]+__top_down(i+1, 0), __top_down(i+1, 1))
            else:
                dp[i][buy] = max(prices[i]-fee+__top_down(i+1, 1), __top_down(i+1, 0))
            return dp[i][buy]
        return __top_down(0, 1)


if __name__ =="__main__":
    s = Solution()
    prices = [1,3,2,8,4,9]
    fee = 2
    print(s.maxProfit(prices, fee))