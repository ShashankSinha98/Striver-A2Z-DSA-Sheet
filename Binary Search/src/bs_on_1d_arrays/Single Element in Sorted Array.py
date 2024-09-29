from typing import List

# (even, odd) -> go right
# (odd, even) -> go left
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        # base case
        if len(nums) == 1 or nums[0] != nums[1]:
            return nums[0]
        elif nums[n-2] != nums[n-1]:
            return nums[n-1]
        
        l, r = 0, n-1
        while l<=r:
            mid = int(l + (r-l)/2)

            # single element case
            if nums[mid-1] < nums[mid] < nums[mid+1]:
                return nums[mid]
            # if mid is even pos
            elif mid % 2 == 0:
                if nums[mid] == nums[mid+1]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] == nums[mid+1]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1


if __name__ == "__main__":
    s = Solution()
    nums = [1,1,2]
    print(s.singleNonDuplicate(nums))
