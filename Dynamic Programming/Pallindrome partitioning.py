class Solution:
    def minCut(self, s):
        def __palindrome_2D(s):
            n = len(s)
            bdp = [[False]*n for _ in range(n)]

            for i in range(n):
                bdp[i][i] = True
                if i<n-1 and s[i]==s[i+1]:
                    bdp[i][i+1]=True
            
            for i in range(2, n):
                for j in range(n-i):
                    if s[j]==s[j+i] and bdp[j+1][j+i-1]==True:
                        bdp[j][j+i] = True
            return bdp

        def __is_palindrome(s, i, j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
            
        n = len(s)
        dp = {}
        bdp = __palindrome_2D(s)
        def __top_down(s, i, j):
            if i>=j or bdp[i][j]:
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]

            min_partitions = len(s)-1
            for k in range(i, j):
                tmp = 1 + __top_down(s, i, k) + __top_down(s, k+1, j)
                min_partitions = min(min_partitions, tmp)
            dp[(i, j)] = min_partitions
            return min_partitions
        
        return __top_down(s, 0, len(s)-1)

if __name__ == "__main__":
    sol = Solution()
    s = "adabdcaebdcebdcacaaaadbbcadabcbeabaadcbcaaddebdbddcbdacdbbaedbdaaecabdceddccbdeeddccdaabbabbdedaaabcdadbdabeacbeadbaddcbaacdbabcccbaceedbcccedbeecbccaecadccbdbdccbcbaacccbddcccbaedbacdbcaccdcaadcbaebebcceabbdcdeaabdbabadeaaaaedbdbcebcbddebccacacddebecabccbbdcbecbaeedcdacdcbdbebbacddddaabaedabbaaabaddcdaadcccdeebcabacdadbaacdccbeceddeebbbdbaaaaabaeecccaebdeabddacbedededebdebabdbcbdcbadbeeceecdcdbbdcbdbeeebcdcabdeeacabdeaedebbcaacdadaecbccbededceceabdcabdeabbcdecdedadcaebaababeedcaacdbdacbccdbcece"
    #s = "abcbd"
    print(sol.minCut(s))