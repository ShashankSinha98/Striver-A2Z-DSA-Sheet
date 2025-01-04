from typing import List

class Solution:
    def jump(self, nums: List[int]) -> bool:
        if len(nums)<2:
            return 0
            
        maxJumpIdx = 0
        c = 0
        for i in range(len(nums)):
            jumpIdx = i + nums[i]
            if jumpIdx > maxJumpIdx:
                c+=1
                maxJumpIdx = jumpIdx
            
            if nums[i]==0 and maxJumpIdx<=i:
                return -1
            
            elif maxJumpIdx>=len(nums)-1:
                return c
        return -1

if __name__ == "__main__":
    s = Solution()
    nums = [2,3,0,1,4]
    nums2 = [0]
    print(s.jump(nums))
