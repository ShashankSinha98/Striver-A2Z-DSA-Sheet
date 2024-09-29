from typing import List
import sys

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = sys.maxsize

        while l <= r:

            mid = int(l + (r - l) / 2)

            if nums[mid] <= nums[r]: # right is sorted
                res = min(res, nums[mid])
                r = mid - 1
            else:
                res = min(res, nums[l])
                l = mid + 1
        
        return res

if __name__ == "__main__":
    s = Solution()
    nums = [11,13,15,17]
    print(s.findMin(nums))
        