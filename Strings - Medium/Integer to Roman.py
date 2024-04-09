class Solution:
    def intToRoman(self, num: int) -> str:
        n = len(str(num))
        base = 10 ** (n-1)
        ans = ""

        while base != 0:
            ans += self.get_roman(num//base, base)
            num = num % base
            base = base // 10
        
        return ans
    
    def get_roman(self, num, base):
        if num <= 3:
            return self.value(base) * num
        elif num == 5:
            return self.value(num*base)
        elif num == 4:
            return self.value(base) + self.value(5*base)
        elif num >= 6 and num <= 8:
            return self.value(5*base) + (self.value(base) * (num-5))
        elif num == 9:
            return self.value(base) + self.value(base*10)
        else:
            return ""

    def value(self, n) -> str:
        match n:
            case 1:
                return 'I'
            case 5:
                return 'V'
            case 10:
                return 'X'
            case 50:
                return 'L'
            case 100:
                return 'C'
            case 500:
                return 'D'
            case 1000:
                return 'M'
            

if __name__ == "__main__":
    num = 1994
    print(Solution().intToRoman(num))