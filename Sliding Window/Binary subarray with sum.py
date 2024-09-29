from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def _numSubarrayLessThanEqualToTarget(target: int) -> int:
            if target < 0:
                return 0
            
            l, r = 0,0
            currSum, count = 0, 0

            while r < len(nums):
                currSum += nums[r]

                while currSum > target:
                    currSum -= nums[l]
                    l+=1
                
                count = count + (r-l+1)
                r+=1
            
            return count
    
        return _numSubarrayLessThanEqualToTarget(goal) - _numSubarrayLessThanEqualToTarget(goal-1)


if __name__ == "__main__":
    s = Solution()
    nums = [0,0,0,0,0]
    goal = 0
    print(s.numSubarraysWithSum(nums, goal))