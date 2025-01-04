class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ni, nj = len(s), len(t)
        def __recursion(i, j) -> int:
            if j==nj:
                return 1
            if i==ni:
                return 0
            
            inc = 0
            if s[i]==t[j]:
                inc = __recursion(i+1, j+1)
            
            return inc + __recursion(i+1, j)
        
        dp = [[-1]*(nj+1) for _ in range(ni+1)]
        def __top_down(i, j) -> int:
            if j==nj:
                return 1
            if i==ni:
                return 0
            
            if dp[i][j]!=-1:
                return dp[i][j]

            inc = 0
            if s[i]==t[j]:
                inc = __top_down(i+1, j+1)
            
            dp[i][j] = inc + __top_down(i+1, j)
            return dp[i][j]
        return __top_down(0, 0)


if __name__ == "__main__":
    sol = Solution()
    #s, t = "babgbag", "bag"
    s, t = "daacaedaceacabbaabdccdaaeaebacddadcaeaacadbceaecddecdeedcebcdacdaebccdeebcbdeaccabcecbeeaadbccbaeccbbdaeadecabbbedceaddcdeabbcdaeadcddedddcececbeeabcbecaeadddeddccbdbcdcbceabcacddbbcedebbcaccac", "ceadbaa"
    print(sol.numDistinct(s,t))