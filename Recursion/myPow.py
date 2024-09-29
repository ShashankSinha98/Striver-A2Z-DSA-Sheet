class Solution:
    def myPow(self, x: float, n: int) -> float:
        def _pow(self, x: float, n: int) -> float:
            if n == 0:
                return 1
            
            if n & 1 == 0: # even
                return _pow(self, x*x, n//2)
            else:
                return x * _pow(self, x, n-1)

        isNeg = n < 0
        ans = _pow(self, x, abs(n))

        return ans if not isNeg else 1/ans


if __name__ == "__main__":
    s = Solution()
    print(s.myPow(2, 2))