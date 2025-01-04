from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def __recusrion(n):
            if n==0:
                return nums[0]
            elif n==1:
                return max(nums[0], nums[1])
            
            return max(nums[n]+__recusrion(n-2), __recusrion(n-1))
        
        dp = [-1]*len(nums)
        def _top_down(n):
            if n==0:
                return nums[0]
            elif n==1:
                return max(nums[0], nums[1])
            
            if dp[n]!=-1:
                return dp[n]
            
            dp[n] = max(nums[n]+_top_down(n-2), _top_down(n-1))
            return dp[n] 
        return _top_down(len(nums)-1)

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3]
    print(s.rob(nums))