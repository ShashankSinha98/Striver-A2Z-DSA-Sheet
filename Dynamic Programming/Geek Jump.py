class Solution:
    def minimumEnergy(self, height, n):
        def __recursion(_n):
            if _n==1:
                return 0
            if _n==2:
                return abs(height[1]-height[0])
            
            return min(__recursion(_n-1) + abs(height[_n-1]-height[_n-2]), __recursion(_n-2) + abs(height[_n-1]-height[_n-3]))
        
        dp = [-1]*(n+1)
        def __top_down(_n):
            if _n==1:
                return 0
            if _n==2:
                return abs(height[1]-height[0])
            
            if dp[_n]!=-1:
                return dp[_n]
            
            dp[_n] = min(__top_down(_n-1) + abs(height[_n-1]-height[_n-2]), __top_down(_n-2) + abs(height[_n-1]-height[_n-3]))
            return dp[_n]
        
        def __bottom_up(_n):
            if _n==1:
                return 0
            first, second = 0, abs(height[1]-height[0])
            if _n==2:
                return second
            
            for i in range(3, _n+1):
                tmp = min(abs(height[i-1]-height[i-2])+second, abs(height[i-1]-height[i-3])+first)
                first = second
                second = tmp
                
            return second

        return __bottom_up(n)


if __name__ == "__main__":
    s = Solution()
    height = [10, 20, 30, 10]
    n = 4
    print(s.minimumEnergy(height, n))