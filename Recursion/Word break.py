from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [[-1]*n for _ in range(n)]

        def _solve(st, end):
            if dp[st][end] != -1:
                return dp[st][end] == 1
            
            if end == len(s)-1:
                ans = s[st:end+1] in wordSet
                return ans

            if s[st: end+1] in wordSet:
                ans = _solve(end+1, end+1)
                if ans:
                    dp[st][end] = 1
                    return True
            
            rec_res = _solve(st, end+1)
            dp[st][end] = 1 if rec_res else 0
            return rec_res
        
        return _solve(0, 0)

if __name__ == "__main__":
    str = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    s = Solution()
    print(s.wordBreak(str, wordDict))        