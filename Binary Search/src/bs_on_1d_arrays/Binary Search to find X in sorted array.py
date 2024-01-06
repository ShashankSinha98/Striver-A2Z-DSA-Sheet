from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = int(l + (r-l)/2)

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
    
if __name__ == "__main__":
    s = Solution()
    nums = [-1,0,3,5,9,12]
    target = 13
    print(s.search(nums, target))