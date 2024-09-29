from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        ans = len(nums)
        while l <= r:
            mid = int(l + (r-l)/2)

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1       
        return ans
    

s = Solution()
nums = [1,3,5,6]
target = 100

print(s.searchInsert(nums, target))