class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        
        val = self.countAndSay(n-1)
        return self.rle(val)
    
    def rle(self, n: str) -> str:
        if len(n)<=0:
            return ""
        
        currChar, currCharCount = n[0], 0
        res = ""
        for i in n:
            if i==currChar:
                currCharCount+=1
            else:
                res += str(currCharCount) + currChar
                currChar = i
                currCharCount = 1
        
        res += str(currCharCount) + currChar
        
        return res
    

if __name__ == "__main__":
    s = Solution()
    n = 4
    ans = s.countAndSay(n)
    print(ans)