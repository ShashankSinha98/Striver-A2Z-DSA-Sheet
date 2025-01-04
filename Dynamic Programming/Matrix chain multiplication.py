import sys

class Solution:
    def matrixMultiplication(self, arr):
        n = len(arr)
        def __recursion(i, j):
            if i>=j:
                return 0
            
            min_cost = sys.maxsize
            for k in range(i, j):
                tmp = __recursion(i, k) + __recursion(k+1, j) + arr[i-1]*arr[k]*arr[j]
                min_cost = min(min_cost, tmp)
            
            return min_cost
        
        dp = [[-1]*(n) for _ in range(n)]
        def __top_down(i, j):
            if i>=j:
                return 0
            
            if dp[i][j]!=-1:
                return dp[i][j]

            min_cost = sys.maxsize
            for k in range(i, j):
                tmp = __top_down(i, k) + __top_down(k+1, j) + arr[i-1]*arr[k]*arr[j]
                min_cost = min(min_cost, tmp)
            dp[i][j] = min_cost
            return min_cost
        
        def __bottom_up():
            dp = [[-1]*(n) for _ in range(n)]
            for i in range(1, n):
                for j in range(1, n):
                    if i>=j:
                        dp[i][j] = 0
            for i in range(n-1, 0, -1):
                for j in range(1, n):
                    if i>=j:
                        continue
                    else:
                        min_cost = sys.maxsize
                        for k in range(i, j):
                            tmp = dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j]
                            min_cost = min(tmp, min_cost)
                        dp[i][j] = min_cost
            #print(dp)
            return dp[1][-1]
        return __bottom_up()
    

if __name__ == "__main__":
    s = Solution()
    arr = [3, 4]
    print(s.matrixMultiplication(arr))
