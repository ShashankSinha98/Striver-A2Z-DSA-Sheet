from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)<2:
            return True
            
        maxJumpIdx = 0
        for i in range(len(nums)):
            jumpIdx = i + nums[i]
            maxJumpIdx = max(maxJumpIdx, jumpIdx)
            
            if nums[i]==0 and maxJumpIdx<=i:
                return False
            
            elif maxJumpIdx>=len(nums)-1:
                return True
        return False

if __name__ == "__main__":
    s = Solution()
    nums = [2,3,1,1,4]
    nums2 = [0]
    print(s.canJump(nums2))
