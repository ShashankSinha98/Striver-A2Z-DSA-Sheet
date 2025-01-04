import sys

class Solution:
    def minimizeCost(self, k, arr):
        def __recursion(n):
            if n<=0:
                return 0
            if n==1:
                return abs(arr[1]-arr[0])
            
            min_cost = sys.maxsize
            for i in range(1, k+1):
                if n-i>=0:
                    tmp = __recursion(n-i) + abs(arr[n]-arr[n-i])
                    min_cost = min(min_cost, tmp)
            return min_cost
        
        dp = [-1]*len(arr)
        def __top_down(n):
            if n<=0:
                return 0
            if n==1:
                return abs(arr[1]-arr[0])
            
            if dp[n]!=-1:
                return dp[n]
            
            min_cost = sys.maxsize
            for i in range(1, k+1):
                if n-i>=0:
                    tmp = __top_down(n-i) + abs(arr[n]-arr[n-i])
                    min_cost = min(min_cost, tmp)
            dp[n] = min_cost
            return dp[n]
        
        def __bottom_up(n):
            dp = [0]*(n+1)
            dp[1] = abs(arr[1]-arr[0])

            for ni in range(2, n+1):
                min_cost = sys.maxsize
                for ki in range(1, k+1):
                    if ni-ki>=0:
                        tmp = dp[ni-ki] + abs(arr[ni]-arr[ni-ki])
                        min_cost = min(min_cost, tmp)
                dp[ni] = min_cost
            return dp[n]
        return __bottom_up(len(arr)-1)

if __name__ == "__main__":
    s = Solution()
    arr = [82, 28, 62, 92, 96, 43]
    k = 6
    print(s.minimizeCost(k, arr))