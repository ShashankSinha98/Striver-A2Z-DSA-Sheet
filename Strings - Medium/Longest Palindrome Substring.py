class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0

        for i in range(len(s)):
            odd_len = self.expand(s, i, i)
            even_len = self.expand(s, i, i+1)

            max_len = max  (even_len, odd_len)
            if max_len > (end-start+1):
                start = i - (max_len-1)//2
                end = i + (max_len) // 2
        
        return s[start: end+1]
    
    def expand(self,  s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return right - left - 1


if __name__ == "__main__":
    s = "racecar"
    print(Solution().longestPalindrome(s))