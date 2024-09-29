class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = start ^ goal
        
        cnt = 0
        for i in range(32):
            if (res & (1<<i)) != 0:
                cnt += 1
        
        return cnt

if __name__ == "__main__":
    s = Solution()
    start, goal = 10, 7
    res = s.minBitFlips(start, goal)
    print(res)