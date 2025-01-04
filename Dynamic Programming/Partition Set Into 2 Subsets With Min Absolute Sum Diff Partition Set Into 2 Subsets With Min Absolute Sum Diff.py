from typing import List
import sys

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        def __bottom_up(nums):
            n = len(nums)
            total = sum(nums)
            # dp = [[False]*(total+1) for _ in range(n+1)]
            dp = [{} for _ in range(n+1)]
            for i in range(n+1):
                _d = dp[i]
                for k in range()
            for i in range(n+1):
                dp[i][0] = True
            
            for i in range(1, n+1):
                for j in range(1, total+1):
                    if nums[i-1]<=j:
                        dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j]
            
            least = sys.maxsize
            for i in range(total//2+1):
                if dp[n-1][i]:
                    first = i
                    second = total-i
                    diff = abs(second-first)
                    least = min(least, diff)
            return least
        return __bottom_up(nums)

if __name__ == "__main__":
    s = Solution()
    nums = [2,-1,0,4,-2,-9] # ans = 0
    print(s.minimumDifference(nums))
        