class Solution:
    def maximumPoints(self, arr, n):
        def __recursion(day, exc=-1):
            # base case
            if day==-1:
                return 0
            
            max_credits = 0
            for k in range(3):
                if k != exc:
                    tmp = arr[day][k] + __recursion(day-1, exc=k)
                    max_credits = max(max_credits, tmp)
            return max_credits
        
        dp = [[-1]*3 for _ in range(n)]
        def __top_down(day, exc=-1):
            # base case
            if day==-1:
                return 0
            if dp[day][exc]!=-1:
                return dp[day][exc]
            max_credits = 0
            for k in range(3):
                if k != exc:
                    tmp = arr[day][k] + __top_down(day-1, exc=k)
                    max_credits = max(max_credits, tmp)
            dp[day][exc] = max_credits
            return dp[day][exc]
        
        def __bottom_up():
            dp = [[0]*3 for _ in range(n)]
            dp[0][0] = max(arr[0][1], arr[0][2])
            dp[0][1] = max(arr[0][0], arr[0][2])
            dp[0][2] = max(arr[0][0], arr[0][1])

            for di in range(1, n):
                for k in range(3):
                    if k==0:
                        dp[di][0] = max(arr[di][1]+dp[di-1][1], arr[di][2]+dp[di-1][2])
                    elif k==1:
                        dp[di][1] = max(arr[di][0]+dp[di-1][0], arr[di][2]+dp[di-1][2])
                    elif k==2:
                        dp[di][2] = max(arr[di][0]+dp[di-1][0], arr[di][1]+dp[di-1][1])
            return max(dp[n-1][0], dp[n-1][1], dp[n-1][2])
        return __bottom_up()


if __name__ == "__main__":
    s = Solution()
    arr = [[1,2,5],[3,1,1],[3,3,3]]
    n = 3
    print(s.maximumPoints(arr, n))