from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1

        # Find start
        start = -1
        while left <= right:
            mid = int(left + (right-left)/2)

            if nums[mid] == target:
                start = mid
                right = mid-1
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        
        if start == -1:
            return [-1, -1]
        
        # Find end
        end = -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = int(left + (right-left)/2)

            if nums[mid] == target:
                end = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1

        return [start, end]
    

s = Solution()
nums = [5,7,7,8,8,10]
target = 2
print(s.searchRange(nums, target))