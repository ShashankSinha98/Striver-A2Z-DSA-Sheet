class Solution:
    def reverseWords(self, s: str) -> str:
        
        tmp = ""
        ans = ""
        s = s.strip()
        n = len(s)
        for i in range(n):
            c = s[i]
            if c != " ":
                tmp += c
            elif tmp != "":
                if ans == "":
                    ans = tmp
                else:
                    ans = tmp + " " + ans
                tmp = ""
        
        if tmp != "":
            if ans == "":
                ans = tmp
            else:
                ans = tmp + " " + ans
        
        return ans 

if __name__ == "__main__":
    s = "   abcd    efgh   "
    print(Solution().reverseWords(s))