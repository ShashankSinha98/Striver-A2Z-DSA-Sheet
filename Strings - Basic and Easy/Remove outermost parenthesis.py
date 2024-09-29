class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        open_bracket_count = 0
        res = ""
        for si in s:
            if si == '(':
                open_bracket_count += 1
            else:
                open_bracket_count -= 1
        
            if open_bracket_count > 1 or (si==')' and open_bracket_count >= 1):
                res += si
        return res
    
if __name__ == "__main__":
    s = "()()"
    ans = Solution().removeOuterParentheses(s)
    print(ans)