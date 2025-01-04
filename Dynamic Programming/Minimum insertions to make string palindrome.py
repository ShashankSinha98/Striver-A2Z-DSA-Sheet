class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        def __recursion(s, i, j):
            if i>=j:
                return 0
            
            if s[i]==s[j]:
                return __recursion(s, i+1, j-1)
            else:
                return 1 + min(__recursion(s, i+1, j), __recursion(s, i, j-1))
        return __recursion(s, 0, n-1)

        dp = [[-1]*(n+1) for _ in range(n+1)]
        def __top_down(s, i, j):
            if i>=j:
                return 0
            
            if dp[i][j]!=-1:
                return dp[i][j]
            
            if s[i]==s[j]:
                dp[i][j] = __top_down(s, i+1, j-1)
            else:
                dp[i][j] = 1 + min(__top_down(s, i+1, j), __top_down(s, i, j-1))
            return dp[i][j]
        return __top_down(s, 0, n-1)


if __name__ == "__main__":
    s = Solution()
    s1 = "leetcode"
    print(s.minInsertions(s1))