class Solution:
    def _rle(self, s: str) -> str:
        res = ""
        currChar = None
        charCount = 0

        for c in s:
            if c == currChar:
                charCount+=1
            else:
                if currChar==None:
                    currChar = c
                    charCount = 1
                else:
                    res += (str(charCount)+currChar)
                    currChar = c
                    charCount = 1
        
        res += (str(charCount)+currChar)
        
        return res
    

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        ans = self.countAndSay(n-1)

        return self._rle(ans)
    

if __name__ == "__main__":
    s = Solution()
    n = 5
    print(s.countAndSay(n))
