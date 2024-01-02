class Solution:
    def isPalindrome(self, s: str) -> bool:
        # def _is_palindrome(self, s: str) -> bool:
        #     if len(s) <= 1:
        #         return True
        #     l = len(s)
        #     return (s[0] == s[l-1]) and _is_palindrome(self, s[1:l-1])
        s = self.preprocess(s)
        l, r = 0, len(s)-1
        
        while l<=r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1

        return True


    def preprocess(self, s: str) -> str:
        res = ""
        for i in s:
            if (i >= 'a' and i<='z') or (i >= 'A' and i<='Z') or (i >= '0' and i<='9'):
                res += i.lower()
        return res

if __name__ == "__main__":
    s = "0P"
    ans = Solution().isPalindrome(s)
    print(ans)