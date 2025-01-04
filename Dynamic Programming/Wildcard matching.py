class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ns, np = len(s), len(p)
        def __onlyStar(p, j):
            while j < len(p):
                if p[j]!='*':
                    return False
                j+=1
            return True
        
        def __recursion(i, j):
            if i==ns: 
                if j==np or __onlyStar(p, j):
                    return True
                else:
                    return False

            if j==np:
                return False
            
            if s[i]==p[j]:
                return __recursion(i+1, j+1)
            else:
                if p[j]=='?':
                    return __recursion(i+1, j+1)
                elif p[j]=='*':
                    return  __recursion(i, j+1) or __recursion(i+1, j) or __recursion(i+1, j+1)
                else:
                    return False

        dp = [[-1]*(np+1) for _ in range(ns+1)]
        def __top_down(i, j):
            if i==ns: 
                if j==np or __onlyStar(p, j):
                    return True
                else:
                    return False

            if j==np:
                return False
            
            if dp[i][j]!=-1:
                return dp[i][j]
            
            if s[i]==p[j]:
                dp[i][j] = __top_down(i+1, j+1)
            else:
                if p[j]=='?':
                    dp[i][j] = __top_down(i+1, j+1)
                elif p[j]=='*':
                    dp[i][j] =  __top_down(i, j+1) or __top_down(i+1, j) or __top_down(i+1, j+1)
                else:
                    dp[i][j] = False
            return dp[i][j]
        return __top_down(0, 0)


if __name__ == "__main__":
    sol = Solution()
    s, p = "adceb", "*a*b"
    print(sol.isMatch(s, p))
        