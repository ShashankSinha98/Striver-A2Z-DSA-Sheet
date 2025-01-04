class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def __bottom_up(s1: str, s2: str) -> int:
            n = len(s1)
            dp = [[0]*(n+1) for _ in range(n+1)]

            for i in range(1, n+1):
                for j in range(1, n+1):
                    if s1[i-1] == s2[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
            return dp[n][n]
        return __bottom_up(s, s[::-1])


if __name__ == "__main__":
    s = Solution()
    s1 = "bbbab"
    print(s.longestPalindromeSubseq(s1))