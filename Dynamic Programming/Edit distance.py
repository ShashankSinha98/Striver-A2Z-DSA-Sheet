class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ni, nj = len(word1), len(word2)
        def __recursion(i, j):
            if i == ni:
                return nj-j
            elif j == nj:
                return ni-i
            
            if word1[i] == word2[j]:
                return __recursion(i+1, j+1)
            else:
                insert = __recursion(i, j+1)
                delete = __recursion(i+1, j)
                replace = __recursion(i+1, j+1)

                return 1 + min(insert, delete, replace)
        
        dp = [[-1]*(nj+1) for _ in range(ni+1)]
        def __top_down(i, j):
            if i == ni:
                return nj-j
            elif j == nj:
                return ni-i
            
            if dp[i][j]!=-1:
                return dp[i][j]
            
            if word1[i] == word2[j]:
                dp[i][j] = __top_down(i+1, j+1)
            else:
                insert = __top_down(i, j+1)
                delete = __top_down(i+1, j)
                replace = __top_down(i+1, j+1)

                dp[i][j] = 1 + min(insert, delete, replace)
            return dp[i][j]
        
        return __top_down(0, 0)


if __name__ == "__main__":
    s = Solution()
    w1, w2 = "intention", "execution"
    print(s.minDistance(w1, w2))
