class Solution:
    def checkValidString(self, s: str) -> bool:
        openBracketCount = 0
        starCount = 0

        for c in s:
            if c == "(":
                openBracketCount+=1
            elif c == "*":
                starCount+=1
            elif c == ")":
                if openBracketCount > 0:
                    openBracketCount -= 1
                elif starCount > 0:
                    starCount -= 1
                else:
                    return False
        
        return openBracketCount-starCount==0
                


if __name__ == "__main__":
    s = Solution()
    print(s.checkValidString("*("))