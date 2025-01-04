class Solution:
    
    def topDown(self, n):
        dp = [-1]*(n+1)
        MOD = 10**9+7
        def __memoized(n):
            if n<=1:
                return n
            
            if dp[n]!=-1:
                return dp[n] % MOD
            
            dp[n] = (__memoized(n-1)%MOD + __memoized(n-2)%MOD)%MOD
            return dp[n]
        return __memoized(n)%MOD

    def bottomUp(self, n):
        if n<=1:
            return n
        MOD = 10**9+7
        first, second = 0, 1
        for i in range(2, n+1):
            tmp = (first + second)%MOD
            first = (second)%MOD
            second = (tmp)%MOD
        return (second)%MOD



if __name__ == "__main__":
    s = Solution()
    n = 6
    for i in range(10):
        if s.topDown(i)!=s.bottomUp(i):
            print("WRONG")
    print("Test completed!")