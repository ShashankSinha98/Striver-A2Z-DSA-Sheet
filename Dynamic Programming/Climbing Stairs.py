class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n
        
        first, second = 1, 2
        for _ in range(3, n+1):
            tmp = first+second
            first = second
            second = tmp
        return second


if __name__ == "__main__":
    s = Solution()
    n = 6
    print(s.climbStairs(n))