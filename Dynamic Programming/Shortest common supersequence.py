class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        ni, nj = len(str1), len(str2)

        def __recursion(i, j):
            if i==ni:
                return str2[j:]
            elif j==nj:
                return str1[i:]
            
            if str1[i]==str2[j]:
                return str1[i] + __recursion(i+1, j+1)
            else:
                l = str1[i] + __recursion(i+1, j)
                r = str2[j] + __recursion(i, j+1)
                if len(l) < len(r):
                    return l
                else:
                    return r
        
        dp = [[-1]*(nj+1) for _ in range(ni+1)]
        def __top_down(i, j):
            if i==ni:
                return str2[j:]
            elif j==nj:
                return str1[i:]
            
            if dp[i][j]!=-1:
                return dp[i][j]

            if str1[i]==str2[j]:
                dp[i][j] = str1[i] + __top_down(i+1, j+1)
            else:
                l = str1[i] + __top_down(i+1, j)
                r = str2[j] + __top_down(i, j+1)
                if len(l) < len(r):
                    dp[i][j] = l
                else:
                    dp[i][j] = r
            return dp[i][j]
        
        def __bottom_up():
            ni, nj = len(str1), len(str2)
            dp = [[""]*(nj+1) for _ in range(ni+1)]
            tmp = ""
            for i in range(1, ni+1):
                tmp+=str1[i-1]
                dp[i][0] = tmp

            tmp = ""
            for j in range(1, nj+1):
                tmp+=str2[j-1]
                dp[0][j] = tmp
            
            for ni in range(1, ni+1):
                for nj in range(1, nj+1):
                    if str1[ni-1]==str2[nj-1]:
                        dp[ni][nj] = dp[ni-1][nj-1] + str1[ni-1]
                    else:
                        l = dp[ni-1][nj]
                        r = dp[ni][nj-1]
                        if len(l) < len(r):
                            dp[ni][nj] = l + str1[ni-1]
                        else:
                            dp[ni][nj] = r + str2[nj-1]
            return dp[ni][nj]

        return __bottom_up()
    
    

if __name__ == "__main__":
    s = Solution()
    s1, s2 = "bcaaacbbbcbdcaddadcacbdddcdcccdadadcbabaccbccdcdcbcaccacbbdcbabb", "dddbbdcbccaccbababaacbcbacdddcdabadcacddbacadabdabcdbaaabaccbdaa"
    #s1, s2 = "abac", "cab"
    print(s.shortestCommonSupersequence(s1, s2))