import sys

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r-l) // 2

            mid_elem = nums[m]
            left_elem = -sys.maxsize if m-1 < 0 else nums[m-1]
            right_elem = -sys.maxsize if m+1 >= len(nums) else nums[m+1]

            if left_elem < mid_elem and right_elem < mid_elem:
                return m
            elif left_elem < mid_elem and right_elem > mid_elem:
                l = m + 1
            elif left_elem > mid_elem and right_elem < mid_elem:
                r = m - 1
            else:
                r = m - 1
        
        return -1

if __name__ == "__main__":
    arr = [1,2,1,3,5,6,4]
    ans = Solution().findPeakElement(arr)
    print(ans)