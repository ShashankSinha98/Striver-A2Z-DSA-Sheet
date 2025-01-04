from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def __bottom_up(nums):
            n = len(nums)
            if n==1:
                return nums[0]
            dp = [0] * (n+1)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n):
                dp[i] = max(nums[i]+dp[i-2], dp[i-1])
            return dp[n-1]
        if len(nums)==1:
            return nums[0]
        return max(__bottom_up(nums[1:]), __bottom_up(nums[:-1]))

if __name__ == "__main__":
    s = Solution()
    nums = [5, 5]
    print(s.rob(nums))
        