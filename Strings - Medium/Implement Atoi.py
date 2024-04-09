class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        i= 0
        s = s.strip()
        n = len(s)
        isNeg = None

        while i < n:
            if s[i] == '+':
                if isNeg is not None:
                    return 0
                isNeg = False
                i+=1
            elif s[i] == '-':
                if isNeg is not None:
                    return 0
                isNeg = True
                i += 1
            elif (s[i] >= '0' and s[i] <= '9'):
                num = int(s[i])
                ans = (ans*10) + num
                #print(ans)
                i+=1

                if not isNeg and ans > (2**31)-1:
                    return (2**31)-1
                elif isNeg and ans > 2**31:
                    return -(2**31)
            else:
                break

        return ans if (isNeg is None or isNeg == False) else -ans
    

if __name__ == "__main__":
    s = "+-32"
    print(Solution().myAtoi(s))