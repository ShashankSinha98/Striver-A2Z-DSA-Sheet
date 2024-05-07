from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digit_map = [0, 0, "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def _solve(idx, curr):
            if idx == len(digits):
                if len(curr) > 0:
                    res.append(curr)
                return
            
            digit_str = digit_map[int(digits[idx])]
            for c in digit_str:
                curr += c
                _solve(idx+1, curr)
                curr = curr[:-1]

        _solve(0, "")
        return res
    

if __name__ == "__main__":
    s = Solution()
    digits = ""
    ans = s.letterCombinations(digits)
    print(ans)