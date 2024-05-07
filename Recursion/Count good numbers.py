class Solution:
    
    def __init__(self) -> None:
        self.mod = 10**9 + 7


    def myPow(self, x: float, n: int) -> float:
        def _pow(self, x: float, n: int) -> float:
            if n == 0:
                return 1
            
            if n & 1 == 0: # even
                return _pow(self, (x*x) % self.mod, n//2)
            else:
                return (x * _pow(self, x, n-1)) % self.mod

        isNeg = n < 0
        ans = _pow(self, x, abs(n))

        return ans if not isNeg else 1/ans
    
    def countGoodNumbers(self, n: int) -> int:
        
        half = n//2

        if n & 1 != 0: 
            return (self.myPow(5, half+1) * self.myPow(4, half)) % self.mod
        else:
            return (self.myPow(5, half) * self.myPow(4, half)) % self.mod
        


if __name__ == "__main__":
    s = Solution()
    print(s.countGoodNumbers(50))
    #print(s.myPow(2, 4))