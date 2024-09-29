class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        sign = -1 if ((dividend<0 and divisor>0) or (dividend>0 and divisor<0)) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        ans, tmp = 0, dividend

        while tmp >= divisor:
            x = 0
            while (1<<x) * divisor <= tmp:
                x += 1
            x-=1

            ans = ans | (1<<x)
            tmp = tmp - ((1<<x)*divisor)
        
        ans = sign*ans
        
        if ans > (1<<31)-1:
            ans = (1<<31)-1
        elif ans < -(1<<31):
            ans = -(1<<31)

        return ans
    

if __name__ == "__main__":
    s = Solution()
    dividend = 7
    divisor = -3

    ans = s.divide(dividend, divisor)
    print(ans)