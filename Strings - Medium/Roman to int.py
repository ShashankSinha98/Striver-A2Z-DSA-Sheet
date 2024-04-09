class Solution:
    def romanToInt(self, s: str) -> int:
        i, ans, n = 0, 0, len(s)

        while i < n:
            if i+1 >= n or self.value(s[i+1]) <= self.value(s[i]):
                ans += self.value(s[i])
                i+=1
            else:
                if i+1 < n and self.value(s[i+1]) > self.value(s[i]):
                    combined_value = (self.value(s[i+1]) - self.value(s[i]))
                    ans += combined_value
                    i+=2
        return ans
    
    def value(self, s: str) -> int:
        match s:
            case 'I':
                return 1
            case 'V':
                return 5
            case 'X':
                return 10
            case 'L':
                return 50
            case 'C':
                return 100
            case 'D':
                return 500
            case 'M':
                return 1000
            case _:
                return None


if __name__ == "__main__":
    s = "MCMXCIV"
    print(Solution().romanToInt(s))