class Solution:
    def myPow(self, x: float, n: int) -> float:
        m = abs(n)
        ans = 1

        while m != 0:
            if (m & 1) == 1:
                ans = ans * x
                m = m - 1
            else:
                m = m // 2
                x = x * x
        
        if n < 0:
            ans = 1 / ans

        return ans

if __name__ == "__main__":
    s = Solution()
    x, n = 2.0, -2
    print(s.myPow(x,n)) 
